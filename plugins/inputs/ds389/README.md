# 389 Directory Server Input Plugin

This plugin gathers metrics from 389 Directory Servers's cn=Monitor backend and cn=monitor,cn=${database},cn=ldbm database,cn=plugins,cn=config for each indexes ans database files.

### Configuration:

```toml
[[inputs.ds389]]
  host = "localhost"
  port = 389

  # ldaps, starttls, or no encryption. default is an empty string, disabling all encryption.
  # note that port will likely need to be changed to 636 for ldaps
  # valid options: "" | "starttls" | "ldaps"
  #protocol = ""

  # skip peer certificate verification. Default is false.
  insecure_skip_verify = false

  # Path to PEM-encoded Root certificate to use to verify server certificate
  tls_ca = "/etc/ssl/certs.pem"

  # dn/password to bind with. If bindDn is empty, an anonymous bind is performed.
  bindDn = ""
  bindPassword = ""
  
  ## Gather dbname to monitor
  # Comma separated list of db filename
  # dbtomonitor = ["exampleDB"]
  # If true, alldbmonitor monitors all db and overrides "dbtomonitor".
  alldbmonitor = false

  # Connections status monitor
  status = false
```

### Measurements & Fields:

All attributes are gathered based on this LDAP query:

`(objectClass=extensibleObject)`

Metric names are attributes name. 

If dbtomonitor array is provided , it can gather metrics for each dbfilename like uniquemember, memberof, givename indexes.
If `alldbmonitor = true`, `dbtomonitor` will be overriden with all dbs currently installed in the Directory Server.

An 389DS 1.3.x server will provide these metrics:

- ds389
  - tags:
    - server
    - port
    - current
    - start
    - version
- fields:
  - currentconnections
  - totalconnections
  - threads
  - currentconnectionsatmaxthreads
  - maxthreadsperconnhits
  - dtablesize
  - readwaiters
  - opsinitiated
  - opscompleted
  - entriessent
  - bytessent
  - anonymousbinds
  - unauthbinds
  - simpleauthbinds
  - strongauthbinds
  - bindsecurityerrors
  - inops
  - readops
  - compareops
  - addentryops
  - removeentryops
  - modifyentryops
  - modifyrdnops
  - listops
  - searchops
  - onelevelsearchops
  - wholesubtreesearchops
  - referrals
  - chainings
  - securityerrors
  - errors
  - connections
  - connectionseq
  - connectionsinmaxthreads
  - connectionsmaxthreadscount
  - bytesrecv
  - bytessent
  - entriesreturned
  - referralsreturned
  - masterentries
  - copyentries
  - cacheentries
  - cachehits
  - slavehits
  - currenttime
  - starttime
  - nbackends

If you enable the Connection status (status = true) a full connection status detail will be added to the metrics.
The idea is to monitor all metrics provided by the 389 Console.

### Connection status metrics

If `status = true` the `connection` attribute will be parsed in this metric:

    - the metric prefix is "conn."
    - the file descriptor is then added to the metric name
    - the name of the monitored parameter is then concatenated with a dot

Format:

`conn.<fd>.<param> = <value>`

### Tags:

- server= # value from config
- port= # value from config
- version= # value from cn=monitor version attribute
- current= # time of measures
- start= # instance start time

### Example Output:

```
$ telegraf-ds389 -config ds389.conf -pollInterval 10s
> ds389,current=20211230141931Z,port=389,server=ldap01,start=20211025142043Z,version=389-Directory/1.3.8.4\ B2019.037.1535 addentryops=0i,anonymousbinds=0i,bindsecurityerrors=3i,bytesrecv=0i,bytessent=190256225i,cacheentries=0i,cachehits=0i,chainings=0i,compareops=0i,conn.64.binddn="NULLDN",conn.64.ip="10.10.15.17",conn.64.opentime="20190704223412Z",conn.64.opscompleted=1i,conn.64.opsinitiated=1i,conn.64.rw="-",conn.65.binddn="NULLDN",conn.65.ip="10.10.15.17",conn.65.opentime="20190704223412Z",conn.65.opscompleted=1i,conn.65.opsinitiated=1i,conn.65.rw="-",connections=6i,connectionseq=86840i,connectionsinmaxthreads=0i,connectionsmaxthreadscount=0i,copyentries=0i,currentconnections=6i,currentconnectionsatmaxthreads=0i,dtablesize=1024i,entriesreturned=259120i,entriessent=259120i,errors=255i,inops=306715i,listops=0i,masterentries=0i,maxthreadsperconnhits=0i,modifyentryops=11i,modifyrdnops=0i,onelevelsearchops=118i,opscompleted=306714i,opsinitiated=306715i,readops=0i,readwaiters=0i,referrals=0i,referralsreturned=0i,removeentryops=0i,searchops=117848i,securityerrors=0i,simpleauthbinds=86815i,slavehits=0i,strongauthbinds=0i,totalconnections=86840i,unauthbinds=3i,wholesubtreesearchops=113152i 1554566915000000000
```
