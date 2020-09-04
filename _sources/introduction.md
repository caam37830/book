# Introduction

You can find a table of contents to your left, or below.

```{tableofcontents}
```

## Preface

This book is designed to be a course reader for STAT 37380 / CAAM 37380 taught at the University of Chicago in the fall quarter of 2020.  The course is designed for students who want to *do* scientific computing, whether they are embarking on a research project in some domain that will require computational components, or want to work on algorithms and implementations to support domain scientists.  Scientific computing is a gateway to a diverse set of topics, including continuous and discrete mathematics, algorithms, computer hardware, programming languages, modeling, simulation, and data analysis.  The student is not expected to be familiar with all of the above when first beginning.  The minimal prerequisites for this course are a solid background in multivariable calculus and linear algebra, some programming experience (not necessarily formally taught), and some exposure to applications such as physics, chemistry, biology, or the social sciences.  An advanced undergraduate or beginning graduate student will likely be prepared.  This course focuses on practical implementations and use, and for the most part leaves theory to other courses aside from some basic notions of what may make one algorithm better than another.

Teaching scientific computing can be a bit challenging because the instructor wants to show students interesting problems as quickly as possible, but also needs to build up many technical skills to solve these problems effectively. This necessarily leads to introducing a mix of ideas at once, and spreading out some topics throughout the course.  The challenge for the student is that their new-found knowledge of a topic like numerical linear algebra may be spread out over many lectures, and mixed in with other areas like optimization or image processing.  This book attempts to help organize this information by putting content for a topic into a single chapter.  The trade-off is that the book is not intended to be read (or taught) sequentially as it appears in the table of contents, an issue that is perhaps mitigated by the online format and ability to add hyperlinks to relevant information across this book.  The potential advantage is that this allows students or instructors to carve their own path through the content without getting too hung up on doing things in the "right" order.  Each chapter begins with the basics and increases in order of complexity.  The chapters of the book are necessarily dependent on each other, but this typically doesn't occur until well into the chapter.  The exceptions are that basic python syntax and computing setup are necessary to do just about anything else.


The course is designed to be taught remotely, out of necessity during the Coronavirus pandemic.  We'll see how it goes.  It is built using [Jupyter Book](https://jupyterbook.org/intro.html).


## What is Scientific Computing?
By definition, computing to support science!  Scientific method (with some computational topics):

1. Ask a question (exploratory data analysis)
2. Formulate a hypothesis (use a model)
3. Design an experiment to test hypothesis (simulation)
4. Analyze data (fit a model, perform uncertainty quantification)

## Why Python?
Python has become an extremely popular language in academia and industry.  Chances are that you will use it at some point in the future no matter where you end up.

1. scripted language, easy to develop in
2. lots of great libraries
3. lots of community support

Languages that fill similar roles as Python for scientific computing: Matlab, R, Julia

If you're serious about scientific computing, I would recommend (at least) learning some C++ after this course, which is the language of choice for performance-critical code, and which is often wrapped by high-level languages (such as Python).  Unfortunately, we can't do everything in a single quarter.


## About this "Book"

This book organizes material into chapters that more or less contain information about a single topic.  This is done in an attempt to organize information in a sensible way.  However, it is not intended to be read or taught in the sequential order seen in the table of contents.  The course will carve some path through the content of the book, and any reader can likewise choose their own adventure through the content.

The chapters are as follows:

<ol start="0">
	<li>Python - syntax, basic packages, basic and advanced topics</li>
	<li> Analysis - asymptotics and convergence</li>
	<li> Linear algebra - dense and sparse</li>
	<li> Optimization - specifying and solving problems</li>
	<li> Functions - root finding, interpolation, calculus on computers</li>
	<li> Graphs - the network kind</li>
	<li> Probability and Statistics - generating random numbers, distributions, parameter estimation</li>
	<li> Data - reading data, visualization, machine learning</li>
	<li> Geometry - metrics, nearest neighbor search, clustering</li>
	<li> Computing - how to use computing resources, how to work with other people</li>
</ol>
