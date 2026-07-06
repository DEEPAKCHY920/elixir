---
name: Cinematic Wellness
colors:
  surface: '#f7f9fb'
  surface-dim: '#d8dadc'
  surface-bright: '#f7f9fb'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f2f4f6'
  surface-container: '#eceef0'
  surface-container-high: '#e6e8ea'
  surface-container-highest: '#e0e3e5'
  on-surface: '#191c1e'
  on-surface-variant: '#424655'
  inverse-surface: '#2d3133'
  inverse-on-surface: '#eff1f3'
  outline: '#727787'
  outline-variant: '#c2c6d8'
  surface-tint: '#0057ce'
  primary: '#0055c9'
  on-primary: '#ffffff'
  primary-container: '#006bfb'
  on-primary-container: '#fefcff'
  inverse-primary: '#b1c5ff'
  secondary: '#006e2d'
  on-secondary: '#ffffff'
  secondary-container: '#7cf994'
  on-secondary-container: '#007230'
  tertiary: '#712ae2'
  on-tertiary: '#ffffff'
  tertiary-container: '#8a4cfc'
  on-tertiary-container: '#fffbff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dae2ff'
  primary-fixed-dim: '#b1c5ff'
  on-primary-fixed: '#001946'
  on-primary-fixed-variant: '#00419e'
  secondary-fixed: '#7ffc97'
  secondary-fixed-dim: '#62df7d'
  on-secondary-fixed: '#002109'
  on-secondary-fixed-variant: '#005320'
  tertiary-fixed: '#eaddff'
  tertiary-fixed-dim: '#d2bbff'
  on-tertiary-fixed: '#25005a'
  on-tertiary-fixed-variant: '#5a00c6'
  background: '#f7f9fb'
  on-background: '#191c1e'
  surface-variant: '#e0e3e5'
  glass-surface: rgba(255, 255, 255, 0.7)
  glass-border: rgba(255, 255, 255, 0.4)
  soft-shadow: rgba(15, 111, 255, 0.08)
  deep-navy: '#034EA2'
typography:
  display-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 64px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  display-lg-mobile:
    fontFamily: Plus Jakarta Sans
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-xl:
    fontFamily: Plus Jakarta Sans
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  label-caps:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.0'
    letterSpacing: 0.1em
  navigation:
    fontFamily: Manrope
    fontSize: 15px
    fontWeight: '500'
    lineHeight: '1.0'
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  container-max: 1440px
  gutter: 32px
  margin-desktop: 80px
  margin-tablet: 40px
  margin-mobile: 20px
  stack-lg: 64px
  stack-md: 32px
  stack-sm: 16px
---

## Brand & Style

This design system embodies a "Cinematic Wellness" aesthetic, merging the precision of high-end SaaS with the ethereal qualities of luxury cosmetic branding. The brand personality is rooted in high-trust innovation, targeting a premium demographic that expects healthcare to feel like a bespoke concierge service rather than a clinical utility.

The visual direction is characterized by **Apple-level cleanliness**—utilizing vast white space, extreme legibility, and a sophisticated interplay of light and depth. We employ a hybrid of **Glassmorphism** and **Soft Neomorphism** to create an environment that feels tactile yet digital, evoking a sense of calm, precision, and technological advancement. The emotional response should be one of immediate relief and absolute confidence in the clinic's cutting-edge capabilities.

## Colors

The palette is anchored by "Clinical White" (#FFFFFF) and "Cloud Gray" (#F8FAFC) to maintain a sterile yet welcoming foundation. **Soft Blue** serves as the primary driver of trust and action, while **Emerald Green** is utilized sparingly for health affirmations and growth indicators. **Purple Accent** provides the luxury "cinematic" edge, used for premium features or high-conversion touchpoints.

Transparency is a core color "state" in this system. Surfaces should rarely be 100% opaque when layered; instead, they use varying degrees of white translucency with backdrop blurs to maintain the glassmorphic feel. Gradients are soft and wide-angled, avoiding harsh transitions to keep the interface feeling fluid and organic.

## Typography

The typographic hierarchy uses **Plus Jakarta Sans** for high-impact headlines to project an approachable yet modern personality. For technical data, UI labels, and navigation, **Manrope** provides a refined, structured feel. **Inter** is reserved for body copy and dense information to ensure maximum legibility and a systematic, SaaS-like clarity.

Tracking should be slightly tightened for large display headers to create a "locked-in" editorial look, while label-level text should have increased letter spacing to improve scannability in dense UI environments.

## Layout & Spacing

The layout philosophy follows a **Fixed-Fluid Hybrid** model. Content is centered within a 1440px max-width container for desktop to maintain "Apple-style" focus, while secondary background elements and glass panels may bleed to the edges of the viewport.

A generous 8px base grid dictates the rhythm. We prioritize vertical breathing room—utilizing large `stack-lg` margins between sections to avoid a "cluttered clinic" feel. Grids are 12-column on desktop, 8-column on tablet, and 4-column on mobile. Components should use dynamic padding that scales, ensuring that internal element spacing (like the gap between an icon and text) remains consistent even as the outer container expands.

## Elevation & Depth

Depth is achieved through a combination of **Ambient Shadows** and **Glassmorphism**. Instead of traditional drop shadows, we use "Glow Shadows"—low-opacity blurs that take on the tint of the primary color (#0F6FFF) to make elements feel as though they are floating on a bed of light.

Soft Neumorphism is applied to interactive elements like cards and buttons. This is achieved through a subtle dual-shadow technique: a highlight shadow (white) on the top-left and a soft neutral shadow on the bottom-right of a container that shares the background color. This creates a "molded" look, as if the UI is physically embossed from the screen. For higher-level overlays, backdrop-filters (blur: 20px) are mandatory to maintain the premium glass effect.

## Shapes

The design system utilizes an aggressive roundedness strategy to soften the medical nature of the content. Base UI elements (buttons, inputs) use a **24px radius** (`rounded-lg`), while large layout containers and cards utilize a **32px-40px radius** (`rounded-xl`). 

Interactive components should feel "squishy" and tactile. Icons are contained within soft-rounded squares or circles. Avoid sharp corners entirely to maintain the approachable, high-end "concierge" aesthetic.

## Components

### Buttons
Primary buttons use the `primary-glow` gradient with a subtle 2px inner-white-border to simulate a glass edge. On hover, the button should lift slightly using a Soft Neumorphic shadow. Secondary buttons are "Ghost Glass"—transparent backgrounds with a 1px `glass-border` and a high backdrop-blur.

### Cards
Cards are the hallmark of this system. They must feature a `glass-surface` background, 20px backdrop blur, and a 1px semi-transparent white border. Content within cards should follow the `stack-md` spacing rule.

### Input Fields
Inputs should appear "recessed" into the surface using an inner shadow (Neumorphic style), with a focus state that transitions the border to `primary_color_hex` and adds a soft blue glow.

### Chips & Tags
Used for medical categories or status. They should be pill-shaped with high-saturation backgrounds at 10% opacity, utilizing the full-color version for the text (e.g., Emerald Green text on 10% Emerald Green background).

### Navigation Bar
A floating glass panel at the top of the viewport. It should have a 40px radius and be narrower than the full screen width, centered with a significant top margin (20px) to enhance the "floating" feel.