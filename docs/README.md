# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a

# Documentation

This library provides functions for calculating area and perimiter of various geometric shapes. The implementation for each shape is located in a separate file.

## Triangle

### Area

`area(a, h)`

Returns area of a triangle with base `a` and height `h`

```
> area(4, 5)
10
```

### Perimiter

`perimiter(a, b, c)`

Returns perimiter of a triangle with sides `a`, `b` and `c`

```
> perimiter(1, 2, 3)
6
```

## Rectangle

### Area

`area(a, b)`

Returns area of a rectangle with sides `a` and `b`

```
> area(4, 3)
12
```

### Perimiter

`perimiter(a, b)`

Returns perimiter of a rectangle with sides `a` and `b`

```
> perimiter(7, 4)
22
```

## Circle

### Area

`area(r)`

Returns area of a circle with radius `r`

```
> area(2)
12.566370614359172
```

### Perimiter

`perimiter(r)`

Returns perimiter of a circle with radius `r`

```
> perimiter(3)
18.84955592153876
```

## Square

### Area

`area(a)`

Returns area of a square with side `a`

```
> area(3)
9
```

### Perimiter

`perimiter(a)`

Returns perimiter of a square with side `a`

```
> perimiter(2)
8
```

# Changelog
- `b5b0fae727ca72c317c383b39c0af73d6adcd81c` L-04: Update docs for calculate.py
- `d76db2ac7f69cc920ae2e6f669fb0671a7fa7d71` L-04: Add calculate.py
- `51c40ebfd0e0b65f52fe5e54740cbb038e492db3` L-04: Doc updated for triangle
- `d080c7888b81955bad2ed78d58ad910526b5132a` L-04: Traingle added
- `d078c8d9ee6155f3cb0e577d28d337b791de28e2` L-03: Docs added
- `8ba9aeb3cea847b63a91ac378a2a6db758682460` L-03: Circle and square added