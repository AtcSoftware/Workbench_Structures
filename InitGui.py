#!/usr/bin/env python
# -*- coding: utf-8 -*-
import FreeCADGui as Gui
import ResourcesPaths as rp


Gui.addLanguagePath(rp.Resources + "/translations")
Gui.updateLocale()

import Loader
Loader.start()
