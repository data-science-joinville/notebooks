#!/usr/bin/env python
# -*- coding: utf-8 -*-

c.NotebookApp.ip = '*'
c.NotebookApp.allow_origin = '*'
c.NotebookApp.open_browser = False
c.NotebookApp.port = 8888

c.IPKernelApp.matplotlib = 'inline'  # https://github.com/conda/conda/issues/1051
