# Overview

[HPCC Systems,](http://HPCCSystems.com) an open source High Performance Computing Cluster, is a massive parallel-processing computing platform that solves Big Data problems. HPCC Systems is an enterprise-proven platform for manipulating, transforming, querying, and data warehousing Big Data. Built by LexisNexis, the HPCC platform has helped it grow to a $1.5 billion information solutions company.

The HPCC Systems architecture incorporates a data query engine (called Thor) and a data delivery engine (called Roxie), as well as common middleware support components, an external communications layer, client interfaces which provide both end-user services and system management tools, and auxiliary components to support monitoring and to facilitate loading and storing of file system data from external sources.

An HPCC environment can include only Thor clusters, or both Thor and Roxie clusters. The HPCC Juju charm creates a cluster which contains both, but you can customize it after deployment.

See [How it Works](http://www.hpccsystems.com/Why-HPCC/How-it-works)  for more details.

See [System Requirements](http://hpccsystems.com/download/docs/system-requirements) for hardware details.
> Please note, your Juju instance must have at least 4GB of RAM. To increase the memory for a unit, run this command:
   `juju set-constraints mem=4G`

The HPCC Juju Charm encapsulates best practice configurations for the HPCC  Systems Platform.  You can use a Juju Charm to stand up an HPCC Platform on:

- Local Provider (LXC)

- Amazon Web Services Cloud


# Usage

## General Usage

1. To deploy a single HPCC Platform node:

    `juju deploy hpccsystems-platform hpcc`

1. When above charm is ready (started) deploy this HPCC Plguins charmL:
    `juju deploy hpccsystems-plugins plugins`

1. To check the status , run
        juju status

1. Add relation to HPCC Platform charm which will performance plugins charm installation and configuration 

    `juju add-relation hpcc plugins`


# Implementation
This charm inherit layer-hpccystems-plugins-base charm. This is a subordinate charm so must be an existing HPCC Platform node or HPCC Cluster node..

![alt Hierarchy Diagram] (images/layer-hpccsystems-plugins.jpg)
  

# HPCC Systems Contact Information

[HPCC Systems Web site](http://HPCCSystems.com)

For support, visit the HPCC Community Forums:
[HPCC Community Forums](http://hpccsystems.com/bb/index.php?sid=0bda2dddb2ea50418357171d33b11e5f)
