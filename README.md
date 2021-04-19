# Telegraf Plugins

This is a collection of Telegraf plugins.

These plugins are now ready_:

- [ds389](plugins/inputs/ds389/README.md): a 389ds metrics collection from cn=monitor.
- [ldap__org](plugins/inputs/ldap_org/README.md): monitor number of entries inside LDAP trees.

## Install Instructions

Download the repository:

$ git clone https://github.com/falon/telegraf-plugins.git

Build the binary:

	$ go build -o telegraf-<plugin_name> cmd/main-<plugin_name>.go

You should then be able to call this from telegraf now using:

```
[[inputs.execd]]
   command = ["/path/to/telegraf-<plugin_name>", "-config", "/etc/telegraf-external/<plugin_name>.conf"
```

### By RPM

As soon as possible
