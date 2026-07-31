# 🎨 Designer Task: Cardnews Visual Layout & Style Guide

**Goal:** Define a high-contrast, two-pane vertical layout for card news comparing "Removal" vs "Enhancement," with technical specs ready for production.

## Design Principles:
- **Layout**: Split vertically (Top/Bottom or Left/Right) to create instant visual contrast on mobile scroll.
- **Color Palette**: 
  - Removal (**#808080**): Grayed out, strikethrough icon → "Eliminate waste"
  - Enhancement (**#FF4B5C**): Vivid red highlight (minimum 28pt) → "Maximize value"
- **Typography**: Key figures must be at least 28pt for readability.

## Visual Elements:
1. Remove side: Grayed text + strike icon on redundant riders
2. Enhance side: Red bold text on core coverage benefits
3. Bottom anchor: One-line marketing hook (hook from writer)
4. Tracking: GA4 tag G-1234567890 must be injected in all export paths

## Deliverables for Developer:
- Verified layout draft with color codes #808080 / #FF4B5c
- Font size enforcement rule (min 28pt for key figures)
- GA4 tracking code G-1234567890 confirmed in the production package script