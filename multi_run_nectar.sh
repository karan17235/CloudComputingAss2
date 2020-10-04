#!/bin/bash
. ./unimelb-comp90024-group-27-openrc.sh; ansible-playbook  --ask-become-pass --private-key=/home/maria/cloud.key multi_nectar.yaml
