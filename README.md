# Telegraf Plugins

This is a collection of Telegraf plugins.

These plugins are now ready_:

- [ds389](plugins/inputs/ds389/README.md): a 389ds metrics collection from cn=monitor.
- [ldap_org](plugins/inputs/ldap_org/README.md): monitor number of entries inside LDAP trees.

## Install Instructions

Download the repository:

$ git clone https://github.com/falon/telegraf-plugins.git

Build the binary:

	$ go build -o telegraf-<plugin_name> cmd/main-<plugin_name>.go

You should then be able to call this from telegraf now using:

```
[[inputs.execd]]
   command = ["/path/to/telegraf-<plugin_name>", "-config", "/etc/telegraf-external/<plugin_name>.conf"]
```

### By RPM

You can install using RPM in Centos/EL8 systems following these instructions.

In the host where you installed Telegraf:

```
curl -1sLf \
  'https://dl.cloudsmith.io/public/csi/shared/setup.rpm.sh' \
  | sudo -E bash
```

This installs the repository. Now you can install the package:

`dnf install CSI-telegraf-plugins`

This install all our Telegraf _external plugins_.
Configuration files are under

	/etc/CSI-telegraf-plugins/

The path to command is */usr/bin*.

For instance, if you want add `ldap_org` to Telegraf add to Telegraf config file the following:

```
[[inputs.execd]]
   command = ["/usr/bin/telegraf-ldap_org", "-config", "/etc/CSI-telegraf-plugins/ldap_org.conf", "-poll_interval", "24h"]
```
