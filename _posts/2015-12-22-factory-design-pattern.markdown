---
layout: post
title: Factory design pattern
date: 2015-12-22 15:22:45.000000000 -05:00
type: post
published: true
status: publish
categories:
- Brain teaser
- Data Structure
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1469276245;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:107;}i:1;a:1:{s:2:"id";i:2049;}i:2;a:1:{s:2:"id";i:1793;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p>[expand title="code"]</p>
<pre>
public class Solution {
    static interface Shape {
        void draw();
    }
    static class Rectangle implements Shape {
        public void draw(){
            System.out.println("Inside Rectangle::draw() method.");
        }
    }
    static class Square implements Shape {
        public void draw() {
            System.out.println("Inside Square::draw() method.");
        }
    }
    static class Circle implements Shape {
        public void draw() {
            System.out.println("Inside Circle::draw() method.");
        }
    }
    static class ShapeFactory {
        public Shape getShape(String shapeType) {
            if (shapeType == null) return null;
            if (shapeType.equals("Rectangle")) {
                return new Rectangle();
            } else if (shapeType.equals("Square")) {
                return new Square();
            } else if (shapeType.equals("Circle")) {
                return new Circle();
            } else {
                return null;
            }
        }
    }
    public static void main(String[] args) {
        ShapeFactory shapeFactory = new ShapeFactory();
        Shape shape1 = shapeFactory.getShape("Rectangle");
        shape1.draw();
        Shape shape2 = shapeFactory.getShape("Square");
        shape2.draw();
        Shape shape3 = shapeFactory.getShape("Circle");
        shape3.draw();
    }
}
</pre>
<p>[/expand]</p>
