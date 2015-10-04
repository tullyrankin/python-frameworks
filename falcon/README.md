# Falcon Web Framework
Falcon is a ridiculously fast, minimalist Python web framework for building cloud APIs and app backends.

The Falcon web framework encourages the REST architectural style, meaning (among other things) that you think in terms of resources and state transitions, which map to HTTP verbs.

You can find more information in the GitHub repo or in the official documentation. We also have a mailing list and IRC channel where you can ask questions and discuss ideas with the community.

Falcon is an Apache-licensed Rackspace community project, built and maintained by a group of stylish volunteers from around the world.

Site: http://falconframework.org/

Github: https://github.com/falconry/falcon

## Routes
```/``` - Index Page

```/hello``` - Hello World!

```/hello/[USER]``` - Hello [USER]!

## Local Installation
```
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```

## Start The Server
```
gunicorn app:api
```
