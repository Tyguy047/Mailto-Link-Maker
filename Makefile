.PHONY: freeze setup run build clean sign zip notarize staple validate

include .env

BUNDLE_ID := com.tylercaselli.mailto-link-maker
APP_NAME := Mailto Link Maker
DMG_NAME := Mailto_Link_Maker

freeze:
	pip freeze > requirements.txt

setup:
	pip install -r requirements.txt

run:
	python main.py

build:
	pyinstaller --windowed --onedir --name "$(APP_NAME)" --icon Assets/MacOS_Icon.icns \
	--osx-bundle-identifier "$(BUNDLE_ID)" \
	main.py

clean:
	rm -rf *.spec dist build *.zip

sign:
	codesign --deep --force --verify --verbose \
	--options runtime \
	--sign "Developer ID Application: $(DEV_ID)" \
	"dist/$(APP_NAME).app"

zip:
	ditto -c -k --keepParent "dist/$(APP_NAME).app" "$(APP_NAME).zip"

notarize:
	xcrun notarytool submit "$(APP_NAME).zip" \
  --apple-id "$(APPLE_ID)" \
  --team-id "$(TEAM_ID)" \
  --password "$(APP_PW)" \
  --wait

staple:
	xcrun stapler staple "dist/$(APP_NAME).app"

validate:
	xcrun stapler validate "dist/$(APP_NAME).app" && spctl -a -vvv -t install "dist/$(APP_NAME).app"

dmg:
	codesign --deep --force --verify --verbose \
	--options runtime \
	--sign "Developer ID Application: $(DEV_ID)" \
	"$(DMG_NAME).dmg"
	xcrun notarytool submit "$(DMG_NAME).dmg" \
	--apple-id "$(APPLE_ID)" \
	--team-id "$(TEAM_ID)" \
	--password "$(APP_PW)" \
	--wait
	xcrun stapler staple "$(DMG_NAME).dmg"