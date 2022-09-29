---
title: Colors
---

# Colors

You can override `css` values to use your own colors by including a 
file called `css/custom.css` in your docs folder 
(this is standard `MkDocs` practice).

## Variables

To use your own color scheme override the variables below:

* `fg` means foreground.
* `bg` means background.

~~~~
:root {

  /* defaults */
  --fg-color: rgb(28, 30, 33);
  --bg-color: rgb(248, 248, 248);
  --font-family: 'Segoe UI', 'Helvetica', 'Arial';

  /* brand */
  --brand-fg-color: #fff;
  --brand-bg-color: #008080;

  /* layout sizing */
  --header-height: 60px;

  /* navbar */
  --navbar-fg-color: var(--brand-fg-color);
  --navbar-bg-color: var(--brand-bg-color);

  /* sidebar */
  --sidebar-fg-color: rgb(96, 103, 112);
  --sidebar-bg-color: rgb(255, 255, 255);
  --sidebar-width: 260px;
  --sidebar-item-active-fg-color: rgb(37, 194, 160);
  --sidebar-item-active-bg-color: rgb(236, 236, 236);
  --sidebar-expanding-item-active-fg-color: rgb(37, 194, 160);
  --sidebar-expanding-item-active-bg-color: var(--sidebar-bg-color);

  /* main */
  --main-fg-color: rgb(28, 30, 33);
  --main-bg-color: rgb(255, 255, 255);
  --main-heading-fg-color: var(--brand-bg-color);
  --main-heading-bg-color: rgb(255, 255, 255);
  --main-margin-left: var(--sidebar-width);
  --main-bold-fg-color: rgb(37, 194, 160);

  /* footer */
  --footer-fg-color: #000;
  --footer-bg-color: #f8f8f8;
  --footer-height: 60px;

}
~~~~

