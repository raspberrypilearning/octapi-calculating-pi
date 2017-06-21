# New project

Each project contains a set of directories for each language, you're set up now with an `en` directory that contains the necessary files to get you going.

* [meta.yml](#metayml)
* [Steps - step_1.md, step_2.md, etc](#steps)


## meta.yml

The `meta.yml` file sets lots of basic information for the project.

``` yml
title: The title of the project
hero_image: images/banner.png # The image used on the listing view and in the project header
description: Project description # Used on the listing view
original_url: https://codeclubprojects.org/en-GB/scratch/rock-band # Provides a link back to the original project
theme: cc-prototype # sets the colour scheme
duration: 1 # 1, 2 or 3
listed: false # A boolean - `true` or`false` - that controls whether the project will appear on the listing view
ingredient: false # A boolean - `true` or`false` - that controls whether the project will appear on the listing view if published to master branch
interests: "jokes/pranks, sports, art/design, photography, games, outside/weather/nature, space, animals, music/sound"
technologies: "scratch, python, html/css, micro:bit"
steps: # A list of all the steps
  - title: How to get started # Used as the sidebar title for the step
```

The list for interests and technologies is generated from the tags defined via the admin site. Once a project is tagged with e.g scratch it will start appearing in the generated list for new projects.

## Steps

* [Links](#links)
* [Resources](#resources)
* [Images](#images)
* [Challenges](#challenges)
* [Definitions](#definitions)
* [Hints](#hints)
* [Collapsed ingredients](#collapsed-ingredients)

Project steps are written in the [Kramdown](https://kramdown.gettalong.org/) variety of markdown. There is a [quick reference guide](https://kramdown.gettalong.org/quickref.html) and [full syntax documentation](https://kramdown.gettalong.org/syntax.html). A [custom kramdown extension](https://github.com/RaspberryPiFoundation/kramdown_rpf) is used for hints, challenges & ingredients.

### Links, resources & images

See [kramdown documentation](https://kramdown.gettalong.org/quickref.html#links-and-images) for more details.

#### Links

A [link](http://kramdown.gettalong.org) to the kramdown homepage.

You can add  a link that opens in a new browser window/tab [like this](https://google.com/){:target="_blank"}

#### Resources

A [link to a file in the resources directory](resources/worksheet.pdf){:download='filename.pdf'}. The download part will make the file automatically download rather than be rendered in the browser, the filename you'd like the file to be saved with is the second bit after the `=`. The `/learning` application will ensure the resource is available.

#### Images

![Banner image](images/banner.png) - the link text becomes the alternative text for the image. The `/learning` application will ensure the image is available.

#### Challenges

``` markdown
--- challenge ---

## Challenge: Improving your drum

* Any markdown in here
* will be parsed as normal

--- /challenge ---
```


### Definitions

Definitions can be written using HTML abbreviations, which are a standard part of [kramdown](https://kramdown.gettalong.org/quickref.html#abbreviations)

```
To do this you might require a variable or a two word definition.

*[variable]: An object that has a name and stores a value.

*[two word]: Definitions are markdown, and can have [links](http://kramdown.gettalong.org) etc
```


### Hints

A header for the hint, and all the html markup for hints will be automatically added.

```
--- hints ---
--- hint ---

Here's a hint of how to do this project.

Any markdown you like within a hint:
* item 1
* item 2

--- /hint ---
--- hint ---
Hint 2

--- /hint ---
--- hint ---

Hint 3
--- /hint ---
--- hint ---
Hint 4
--- /hint ---

--- /hints ---
```

### Ingredients

An ingredient is a bit of reusable content from another project. All ingredients appear collapsed to users, the title for the collapsed element is the title of the ingredient project.

To add an ingredient to your content:
```
[[[generic-scratch-new-project]]]
```
