# Design System: The Editorial Archive

## 1. Overview & Creative North Star: "The Curated Memory"
This design system is built to transcend the ephemeral nature of digital invitations, positioning itself as a permanent digital artifact. The Creative North Star is **"The Curated Memory"**—a philosophy that treats every screen like a spread in a high-fashion boutique magazine.

To break the "template" look, this system rejects rigid symmetry in favor of **Intentional Asymmetry**. Elements should feel like they were placed by a human hand: a headline may be slightly offset to the left, while an image sits anchored to the bottom-right, separated by a sea of purposeful white space. We avoid the "boxed-in" feel of standard web grids by allowing elements to overlap slightly, creating a sense of depth and tactile layering reminiscent of a physical scrapbook or a fashion editorial layout.

---

## 2. Colors: Tonal Depth & The "No-Line" Rule
The palette is a sophisticated interplay of warmth and weight. We move away from digital "pure whites" into a world of creamy, organic textures.

*   **Primary Palette:** `primary` (#7e5139) and `primary_container` (#9a6950) serve as our terracotta anchors, used for moments of warmth and call-to-action focus.
*   **Neutral Palette:** The `surface` series (Butter Cream #fdf9f4) provides the canvas. Use `on_surface` (#1c1c19 / Charcoal) for high-contrast legibility.

### The "No-Line" Rule
Standard 1px borders are strictly prohibited for sectioning. Boundaries must be defined through **Background Color Shifts**. 
*   Transition from `surface` to `surface_container_low` to mark a change in content.
*   **Surface Hierarchy:** To create "nested" depth, treat the UI as stacked sheets of fine cotton paper. An RSVP card (`surface_container_lowest`) should sit atop a `surface_container` background, creating a soft, natural lift.

### Signature Textures & Glass
To evoke "quiet luxury," use **Glassmorphism** for floating navigation or modal overlays. Utilize `surface` colors at 80% opacity with a `20px` backdrop-blur. Apply a subtle linear gradient from `primary` to `primary_container` (15% opacity) over hero sections to simulate the grainy, chromatic variance of 35mm film.

---

## 3. Typography: The Jewelry & The Document
Typography is the cornerstone of this system. It is divided into two distinct personalities:

*   **The Jewelry (Display & Headline):** Using the **Newsreader** high-contrast serif. This is our "jewel." Headlines should be treated as art pieces. Use `display-lg` for names and dates, ensuring tight kerning for a bespoke, editorial feel. 
*   **The Document (Body & Labels):** Using **Work Sans**. This is our functional anchor. To achieve the "high-fashion" look, increase `letter-spacing` by 0.05em for `body-md` and `label-md`. This creates an airy, legible, and premium reading experience.

**Hierarchy Goal:** The contrast between the dramatic, sharp serifs and the clean, wide sans-serif communicates authority and timelessness.

---

## 4. Elevation & Depth: Tonal Layering
We do not use shadows to simulate height; we use **Tonal Layering**.

*   **The Layering Principle:** Place a `surface_container_lowest` element on a `surface_container_low` background. This creates a "soft lift" that feels architectural rather than digital.
*   **Ambient Shadows:** If a floating element (like a gallery light-box) requires a shadow, it must be nearly invisible. Use `on_surface` at 4% opacity with a `40px` blur and `0px` offset. It should feel like a soft glow of light, not a shadow.
*   **The "Ghost Border":** If accessibility requires a stroke, use `outline_variant` at 20% opacity. Never use a 100% opaque border; it breaks the "airy" atmosphere of the system.

---

## 5. Components: Editorial Primitives

### Buttons
*   **Primary:** Rectangular, sharp 0px corners (`DEFAULT: 0px`). Background: `primary`. Text: `on_primary` (Work Sans, All Caps, 1px letter spacing).
*   **Tertiary (The "Editorial" Link):** No background. `on_surface` text with a 1px underline that sits 4px below the baseline.

### Cards & Content Blocks
*   **Rule:** Forbid divider lines. Separate content using the **Spacing Scale** (increments of 16px/24px/48px). 
*   **Asymmetric Cards:** Images should not always be centered. Place an image in a card with 0px padding on one side and 40px on the other to create an editorial "bleed" effect.

### Input Fields
*   **Style:** Minimalist. Only a bottom border using `outline` (#83746d). Labels (`label-md`) should sit above the line in `on_surface_variant`. 
*   **Focus State:** The bottom border transitions to `primary` (#7e5139). No "glow" or "outline" rings.

### Relevant Custom Components
*   **The Timeline:** Use a single, vertical 1px line in `outline_variant` (30% opacity) to connect events, punctuated by small `primary` dots.
*   **The Grain Overlay:** A global fixed `div` with a noise texture at 3% opacity to give the entire UI a nostalgic film aesthetic.

---

## 6. Do’s and Don’ts

### Do:
*   **Do** embrace white space. If a section feels "full," double the padding.
*   **Do** use `0px` border-radius for everything. Sharp corners equal high-fashion sophistication.
*   **Do** use asymmetrical margins (e.g., `margin-left: 10%`, `margin-right: 20%`) for text blocks to mimic magazine layouts.

### Don’t:
*   **Don’t** use "Drop Shadows" from standard UI kits.
*   **Don’t** use rounded corners (`border-radius`). It diminishes the "High-Fashion Editorial" intent.
*   **Don’t** use pure black (#000). Always use `on_surface` (#1c1c19) or `secondary` (#5f5e5e) to maintain the "Warm Minimalism" feel.
*   **Don’t** center-align everything. Modern editorial design thrives on the tension between different alignment axes.