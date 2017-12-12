#!/usr/bin/env python3
#
# @file: passive_image_enhancer.py
# @description: Enhance Multiple Images with special blending
# @author: Loouis Low
# @license: MIT
# @copyright:
#

from PIL import Image, ImageFilter, ImageEnhance, ImageDraw

import os, sys

path = "/path/to/your/images/"
dirs = os.listdir(path)

def enhancer():
  for image in dirs:
    if os.path.isfile(path+image):
      source = Image.open(path+image)
      f, e = os.path.splitext(path+image)

      # filters
      filter1 = source.filter(ImageFilter.DETAIL)
      filter2 = source.filter(ImageFilter.FIND_EDGES)
      
      # blend 2 filters
      compose = Image.blend(filter1, filter2, alpha=.1)
      
      # final blend with smoothness
      filter3 = source.filter(ImageFilter.SMOOTH)
      blend = Image.blend(compose, filter3, alpha=.1)

      # color          
      imageColor = ImageEnhance.Color(blend)
      renderStage1 = imageColor.enhance(1.5)
      
      # contrast          
      imageContrast = ImageEnhance.Contrast(renderStage1)
      renderStage2 = imageContrast.enhance(1.1)
      
      # brightness          
      imageBrightness = ImageEnhance.Brightness(renderStage2)            
      renderFinal = imageBrightness.enhance(1.1)            

      # write to file
      renderFinal.save(f + '_enhanced.jpg', 'JPEG', quality=100)

enhancer()
