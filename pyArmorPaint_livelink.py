# -*- coding: utf8 -*-
# python
# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

"""
ArmorPaint LiveLink is a tool to directly load your Assets into ArmorPaint

Usage:
import pyArmorPaint_livelink
pyArmorPaint_livelink.show()
"""

__author__ = 'Leo DEPOIX (leonumerique@gmail.com)'
__version__ = '1.0.0'
__date__ = '2020/03/11'
__copyright__ = 'Copyright (c) 2020 Leo DEPOIX'

import sys
import maya.api.OpenMaya as om
import maya.mel

from maya import cmds

import os, subprocess, platform

# Private constants
_default_size = (44, 74)
_preferences_size = (200, 25)

# Global constants
path_base = " "


# icons path
_icons_path = os.path.join(os.path.dirname(__file__), 'icons')

def cb(method, *args):
    """Easy-call UI callback method."""

    return lambda *x: method(*args)

def getActiveObjectName():
    """Get list of active objects"""
    sl = cmds.ls(sl=1, o=1)
    
    """
    for s in sl:
        print s
    """
    return sl[0]
   
def getMayaProjectDir():
    dir = maya.mel.eval('workspace -q -rd;')
    return dir

def launchArmorPaint(path_base):
    """Start ArmorPaint Function"""
    
    #Check if ArmorPath Exist
    if path_base == " ":
        sys.stdout.write('Please select ArmorPaint Installation directory in Preferences')
        return False
    
    #Check if an object is selected
    if cmds.ls(sl=True):
        object = getActiveObjectName()
        cmds.select(clear=True)
        cmds.select(object)
        
        armorpaintFile = getMayaProjectDir() + "/sourceimages/" + object + ".arm"
        
        #Generating Paths for each OS
        if platform.system() == "Windows":
            path_base = path_base.replace("/","\\\\")
            armorpaintFile = armorpaintFile.replace("/","\\\\") 
            path_tmp = path_base + "\\\data\\\\tmp.obj"
            path_exe = path_base + "\\\ArmorPaint.exe"
        elif platform.system() == "Linux":
            path_tmp = path_base + "/data/tmp.obj"
            path_exe = path_base + "/ArmorPaint"
        elif platform.system() == "Darwin":
            path_tmp = path_base + "/data/tmp.obj"
            path_exe = path_base + "/ArmorPaint"
        
        if os.path.isfile(armorpaintFile):
            print ("File exist")
            #Launch ArmorPaint
            subprocess.Popen([path_exe,armorpaintFile])
            
        else:
            print ("File not exist")
            #Maya export to obj
            maya.cmds.loadPlugin("objExport.mll") #Load obj exporter
            mel_obj_export_command = "file -force -options \"groups=1;ptgroups=1;materials=1;smoothing=1;normals=1\" -type \"OBJexport\" -pr -es \"" + path_tmp + "\";"
            maya.mel.eval(mel_obj_export_command)

            #Launch ArmorPaint
            subprocess.Popen([path_exe,path_tmp])
            sys.stdout.write('Please save your ArmorPaint file here: %s' % armorpaintFile)
    else:
        sys.stdout.write('Please select an object!')
        
def ArmorPaintDirFileDialog():
    global path_base

    singleFilter = "All Files (*.*)"
    path_base = cmds.fileDialog2(caption="Open ArmorPaint Directory",fileFilter=singleFilter, dialogStyle=2, fileMode=3)[0]

    sys.stdout.write('\nArmorPaint directory as been changed: %s' % path_base)
    sys.stdout.write('\nPlease re-open the UI')
    cmds.deleteUI("ArmorPaintLiveLink", window=True )

def show(width=_default_size[0], height=_default_size[1]):
    """Main UI."""
    
    win_name = 'ArmorPaintLiveLink'
    if cmds.window(win_name, exists=True):
        cmds.deleteUI(win_name, window=True)
    
    cmds.window(win_name, title='ArmorPaintLiveLink', tlb=True)
    cmds.columnLayout(adj=True, rs=0, bgc=(0.3, 0.3, 0.3))
    
    # BUTTONS #
    cmds.iconTextButton(style='iconOnly', h=34, bgc=(0.3, 0.3, 0.3), image=os.path.join(_icons_path, 'ArmorPaintLogo.xpm'),
                        c=cb(launchArmorPaint, path_base), ann='Paint selected')
    
    cmds.iconTextButton(style='iconOnly', h=34, bgc=(0.3, 0.3, 0.3), image=os.path.join(_icons_path, 'Preferences.xpm'),
                        c=cb(ArmorPaintDirFileDialog), ann='Prerences')
    
    cmds.showWindow(win_name)
    cmds.window(win_name, edit=True, widthHeight=(width, height))
    
    sys.stdout.write('ArmorPaint Live Link %s          https://github.com/PiloeGAO          leonumerique@gmail.com\n'
                     % __version__)