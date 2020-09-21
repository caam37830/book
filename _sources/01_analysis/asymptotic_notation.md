# Asymptotic Notation

First, let's review some asymptotic notation.  We'll see it a fair amount

Let $f(x), g(x)$ be some functions.  We say
$$f = O(g)$$
as $x\to \infty$ if there exists some constant $c\ge 0$ and $x_0\ge 0$ so that $ |f(x)| \le c g(x) )$ for all $x \ge x_0$.

We say
$$f = \Omega(g)$$
as $x\to \infty$ if there exists some constant $c\ge 0$ and $x_0\ge 0$ so that $ |f(x)| \ge c g(x) )$ for all $x \ge x_0$.

Finally,
$$f = \Theta(g)$$
if $f = O(g)$ and $f = \Omega(g)$ (some constant multiples of $g$ bound $f$ above and below).

Often we're interested in bounding worst-case behavior.  This means you'll see a lot of $O()$, and less of $\Omega$ and $\Theta$.

Note that because we can scale by constant multiples, we typically drop them.
1. $O(5x) = O(x)$
2. $O(c = O(1)$
3. $O(c f(x)) = O(f(x))$

## Examples

1. $x = O(x)$
2. $x = O(x^2)$
3. $x^a = O(x^b)$ for $a \le b$
4. $x^a = O(b^x)$ for any $a, b > 0$
