---
layout: post
title: Factory design pattern
date: 2015-12-22 15:22:45.000000000 -05:00
tags:
- Leetcode
categories:
- Brain Teaser
- Data Structure
author: Jason
---
<p><strong><em>Factory design pattern</em></strong></p>


``` java
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
```
