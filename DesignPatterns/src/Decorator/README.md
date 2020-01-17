###Decorator Pattern
Motivated based on your need to augment an object with additional functionality
without rewriting existing code(violated OCP Principle), and you want to keep the new functionality separate(SRP).  

Two options: 
1. Inherit from required object if possible.
2. Build a Decorator, which simply references the decorated object(s).  

**Dynamic Decorator**:  
In our example, when we want to add color to existing shape, we create a new class **ColoredShape** 
and take Shape as parameter in its constructor, and take color as another parameter. That way we can 
create a new **ColoredShape** with existing shape and the color we want.

