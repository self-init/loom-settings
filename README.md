# Extensible settings app for Linux.

This app works by taking in schemas that define the config file(s) of a programs.
The app then provides a UI to modify the config files based on the contents of the schema.
Schemas are loaded dynamically allowing users to add support to their favorite programs.

## Roadmap

1. Implement MVP with 1/2 file formats and 1/2 schemas
2. Add more functionality to schemas including managing differences across versions and distros
3. Experiment with remote management features
4. Experiment with other components (i.e. package management, systemd services)
5. If component experimentation is successful, transition to a Model View ViewModel Architecture
