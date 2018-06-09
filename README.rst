==============
Language-Flags
==============

Flags is a simple Django app that helps display national flags. For
efficiency, there is just one huge PNG file with all the flags, and
individual flags are selected for display using CSS trickery.

Quick start
-----------

1. Add "language_flags" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
	'language_flags',
    ]

2. In templates where you want to use language_flags, include the
   language_flags template tag library::

    {% load language_flags_tags %}

   and include css or min.css in HTML ``<head>``::

    <link rel="stylesheet" type="text/css" href="{% static 'css/flags.css' %}">

   Don't forget ``{% load staticfiles %}`` at the top of your template.


3. You can use the `flags_for_language` tag to display a number
   of flags of nations where a language is spoken. Right now the
   language can be either English or German::

    {% flags_for_language COUNT LANGUAGE %}

   This will display COUNT flags for language LANGUAGE; the flags will
   always include the first country listed for LANGUAGE, while the
   remainder will be randomly selected from the other countries.

Acknowledgments
---------------

The flag sprite was downloaded from https://www.flag-sprites.com and
is derived from the FamFamFam flag icon set at
http://www.famfamfam.com/lab/icons/flags/.
