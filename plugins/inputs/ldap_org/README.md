# ldap_org
## Input plugin to monitor your 389 (Red Hat) Directory Server population

This plugin gathers metrics from 389 Directory Server's backend. It is based on work made for Openldap Input Plugin.

Let suppose to have these trees:

- dn: o=myorg,cn=en

- dn: ou=myfirstdomain,o=myorg,cn=en

- 	dn: uid=user1,ou=myfirstdomain,o=myorg,cn=en

- 	dn: uid=user2,ou=myfirstdomain,o=myorg,cn=en

- dn: ou=myseconddomain,o=myorg,cn=en

- 	dn: uid=user1,ou=myseconddomain,o=myorg,cn=en

- ...

You need to track number of entries on each subtree of o=myorg,cn=en based on ou=<domain> path.
You could need to count all entries `(objectClass=*)` or only ones returned by a filter.

### Configuration:
```
# LDAP Count by Org plugin
[[inputs.ldap_org]]
  # LDAP Host and post to query
  host = "localhost"
  port = 389

  # ldaps, starttls, or no encryption. default is an empty string, disabling all encryption.
  # note that port will likely need to be changed to 636 for ldaps
  # valid options: "" | "starttls" | "ldaps"
  tls = ""

  # skip peer certificate verification. Default is false.
  insecure_skip_verify = false

  # Path to PEM-encoded Root certificate to use to verify server certificate
  tls_ca = "/etc/ssl/certs.pem"

  # dn/password to bind with. If bindDn is empty, an anonymous bind is performed.
  bindDn = ""
  bindPassword = ""

  # Where to count metrics
  # For instance ou=<metric_name>,o=myorg,c=en
  # In searchBase look for "retAttr=*", then for each DN look for Filter and count results.
  searchBase = "o=myorg,c=en"
  retAttr = "ou"
  filter = "(objectClass=*)"
```
You probably must define a bind with appropriate ACI.

### Tags:

    server= # value from config
    port= # value from config
    base= # value from <searchBase> configuration  attribute
    
### Example Output:

```
$ telegraf-ldap_org -config ldap_org.conf -pollInterval 24h
2019-07-08T12:03:41Z I! Starting Telegraf 1.11.1
> ldap_org,base=o\=myorg\,c\=en,host=telegraf.example.com,port=389,server=ldap.example.com myfirstdomain=2i,myseconddomain=1i 1562587461000000000
```
