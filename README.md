# Mailto Link Maker

A free and open source tool to quickly create `mailto` links. Built with Python and tkinter, it provides a simple GUI where you enter an email address, subject, and body — then generates a ready-to-use `mailto:` link.

## Supported Platforms

Mailto Link Maker should run on all platforms, but it is currently only packaged for macOS (and properly signed to avoid Gatekeeper warnings). Using the `Makefile`, you can build it for macOS yourself, or use PyInstaller commands directly to run it on Linux or Windows.

*When building with the `Makefile`, you can ignore the signing steps, since those are only used for publishing releases.* Run:

```bash
make build
```

Your built app will be available in the `dist` folder.

## Credits

Developed by **Tyler Caselli**

- Website: [https://tylercaselli.com](https://tylercaselli.com)

## License

This project is licensed under the [Mozilla Public License Version 2.0](LICENSE).
