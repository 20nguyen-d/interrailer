import tkinter as tk
from tkinter import ttk
import random


# ============================================================
# TMUA FLASHCARD BANK
# Format:
# ("Category", priority 1-3, "Front", "Back")
# ============================================================

CARDS = [

    # =========================
    # ALGEBRA
    # =========================

    ("Algebra", 3,
     "I see 1/x + 1/y = 1/n. What should I try?",
     "Manufacture a product.\n\n"
     "xy = n(x + y)\n"
     "xy - nx - ny = 0\n"
     "(x - n)(y - n) = n^2\n\n"
     "Then use factor pairs / divisors."),

    ("Algebra", 3,
     "A quadratic is stated to have INTEGER roots. What should I think?",
     "The discriminant must be a perfect square.\n\n"
     "Δ = b^2 - 4ac = k^2\n\n"
     "Then try turning a difference of squares into factor pairs."),

    ("Algebra", 3,
     "How does the discriminant tell me the number of real roots?",
     "For ax^2 + bx + c = 0:\n\n"
     "Δ > 0  →  2 distinct real roots\n"
     "Δ = 0  →  1 repeated real root\n"
     "Δ < 0  →  no real roots"),

    ("Algebra", 3,
     "What are Vieta's formulas for ax^2 + bx + c = 0?",
     "If the roots are α and β:\n\n"
     "α + β = -b/a\n"
     "αβ = c/a\n\n"
     "Often much faster than explicitly solving the quadratic."),

    ("Algebra", 3,
     "I know x + y = s and xy = p. What representation should I use?",
     "x and y are the roots of\n\n"
     "t^2 - st + p = 0.\n\n"
     "For real x,y, require:\n"
     "s^2 - 4p ≥ 0."),

    ("Algebra", 3,
     "I see x^4, x^2 and constants. What should this trigger?",
     "A hidden quadratic.\n\n"
     "Let u = x^2.\n\n"
     "Then solve the quadratic in u, remembering u ≥ 0."),

    ("Algebra", 3,
     "I see x + 1/x repeatedly. What substitution might help?",
     "Let u = x + 1/x.\n\n"
     "Then:\n"
     "x^2 + 1/x^2 = u^2 - 2\n\n"
     "x^3 + 1/x^3 = u^3 - 3u"),

    ("Algebra", 3,
     "Why is difference of two squares so useful in integer problems?",
     "x^2 - y^2 = (x-y)(x+y).\n\n"
     "It turns an equation into a factor-pair problem.\n\n"
     "Also, x-y and x+y have the SAME parity."),

    ("Algebra", 2,
     "Factorise a^2 - b^2.",
     "(a-b)(a+b)"),

    ("Algebra", 2,
     "Factorise a^3 - b^3.",
     "(a-b)(a^2 + ab + b^2)"),

    ("Algebra", 2,
     "Factorise a^3 + b^3.",
     "(a+b)(a^2 - ab + b^2)"),

    ("Algebra", 2,
     "If P(a) = 0, what does the factor theorem tell me?",
     "x - a is a factor of P(x)."),

    ("Algebra", 2,
     "What is the remainder when P(x) is divided by x-a?",
     "P(a)."),

    ("Algebra", 3,
     "A parameter k changes the NUMBER of solutions. What should I think?",
     "Think GRAPHICALLY.\n\n"
     "Number of solutions = number of intersections.\n\n"
     "Boundary cases often occur at tangency:\n"
     "f(x) = g(x)\n"
     "and\n"
     "f'(x) = g'(x)\n\n"
     "For a quadratic, this is often Δ = 0."),

    ("Algebra", 2,
     "Why might completing the square help?",
     "It reveals the vertex / minimum / maximum immediately.\n\n"
     "x^2 + bx + c\n"
     "= (x + b/2)^2 + c - b^2/4"),

    ("Algebra", 2,
     "A problem is homogeneous and only ratios seem to matter. Possible trick?",
     "Scale one variable away.\n\n"
     "For example, set y = 1 or let t = x/y,\n"
     "provided the denominator is non-zero."),


    # =========================
    # INEQUALITIES / MODULUS
    # =========================

    ("Inequalities & Modulus", 3,
     "Can I multiply an inequality by x?",
     "ONLY if you know the sign of x.\n\n"
     "If the sign is unknown, multiplying can reverse the inequality.\n\n"
     "Instead, move everything to one side and use a sign chart."),

    ("Inequalities & Modulus", 3,
     "How should I solve a rational inequality like f(x)/g(x) > 0?",
     "1. Find zeros of f(x).\n"
     "2. Find zeros of g(x).\n"
     "3. Put all critical values on a number line.\n"
     "4. Test signs in each interval.\n"
     "5. Remember g(x) ≠ 0."),

    ("Inequalities & Modulus", 3,
     "What does |x| < a mean, for a > 0?",
     "-a < x < a"),

    ("Inequalities & Modulus", 3,
     "What does |x| > a mean, for a > 0?",
     "x < -a  OR  x > a"),

    ("Inequalities & Modulus", 3,
     "How do I solve |f(x)| = a?",
     "Split into two equations:\n\n"
     "f(x) = a\n"
     "OR\n"
     "f(x) = -a"),

    ("Inequalities & Modulus", 3,
     "What is √(x^2)?",
     "|x|\n\n"
     "NOT simply x."),

    ("Inequalities & Modulus", 3,
     "What danger comes from squaring both sides of an equation?",
     "Squaring can introduce extraneous solutions.\n\n"
     "Always substitute final answers back into the ORIGINAL equation."),

    ("Inequalities & Modulus", 2,
     "How do I rationalise 1/(√a + √b)?",
     "Multiply top and bottom by the conjugate:\n\n"
     "√a - √b\n\n"
     "because\n"
     "(√a + √b)(√a - √b) = a-b."),

    ("Inequalities & Modulus", 3,
     "Positive x,y have fixed x+y. When is xy largest?",
     "When x = y.\n\n"
     "AM-GM gives:\n"
     "xy ≤ ((x+y)/2)^2."),

    ("Inequalities & Modulus", 3,
     "Positive x,y have fixed xy. When is x+y smallest?",
     "When x = y.\n\n"
     "AM-GM:\n"
     "x+y ≥ 2√(xy)."),

    ("Inequalities & Modulus", 2,
     "Why should I check the equality case of an inequality?",
     "It tells you whether the bound is achievable and often identifies the extremal case."),


    # =========================
    # FUNCTIONS / GRAPHS
    # =========================

    ("Functions & Graphs", 3,
     "I need to compare f(x) and g(x). What is a useful transformation?",
     "Define\n\n"
     "h(x) = f(x) - g(x).\n\n"
     "Then:\n"
     "f > g  ↔  h > 0\n"
     "f = g  ↔  h = 0"),

    ("Functions & Graphs", 3,
     "If f'(x) > g'(x), must f(x) > g(x)?",
     "NO.\n\n"
     "It means:\n"
     "(f-g)' > 0\n\n"
     "so f(x)-g(x) is increasing.\n\n"
     "An increasing difference does not have to be positive."),

    ("Functions & Graphs", 3,
     "What does f'(x) > 0 mean?",
     "f is increasing.\n\n"
     "It does NOT mean f(x) > 0."),

    ("Functions & Graphs", 3,
     "What does f''(x) > 0 mean?",
     "f is convex / concave upwards.\n\n"
     "Equivalently, f'(x) is increasing.\n\n"
     "It does NOT necessarily mean f is increasing."),

    ("Functions & Graphs", 3,
     "What does the number of solutions to f(x)=g(x) represent graphically?",
     "The number of intersections of the graphs y=f(x) and y=g(x)."),

    ("Functions & Graphs", 3,
     "Transformation: y = f(x) + a",
     "Translate the graph UP by a."),

    ("Functions & Graphs", 3,
     "Transformation: y = f(x-a)",
     "Translate the graph RIGHT by a.\n\n"
     "Inside transformations act in the opposite direction."),

    ("Functions & Graphs", 3,
     "Transformation: y = a f(x)",
     "Vertical scale factor |a|.\n\n"
     "If a < 0, also reflect in the x-axis."),

    ("Functions & Graphs", 3,
     "Transformation: y = f(ax)",
     "Horizontal scale factor 1/|a|.\n\n"
     "If a < 0, also reflect in the y-axis."),

    ("Functions & Graphs", 3,
     "Point mapping for y = a f(b(x-h)) + k?",
     "(x, y) maps to:\n\n"
     "(x/b + h,  ay + k)"),

    ("Functions & Graphs", 3,
     "What happens to y = |f(x)|?",
     "Any part of f below the x-axis is reflected ABOVE the x-axis.\n\n"
     "Positive parts stay unchanged."),

    ("Functions & Graphs", 3,
     "What happens to y = f(|x|)?",
     "Keep the RIGHT half of f and reflect it into the left half.\n\n"
     "The resulting graph is even."),

    ("Functions & Graphs", 3,
     "Definition of an even function?",
     "f(-x) = f(x)\n\n"
     "Graph has symmetry about the y-axis."),

    ("Functions & Graphs", 3,
     "Definition of an odd function?",
     "f(-x) = -f(x)\n\n"
     "Graph has 180° rotational symmetry about the origin."),

    ("Functions & Graphs", 2,
     "I cannot visualise a graph. Which features should I find first?",
     "Find anchor information:\n\n"
     "• domain\n"
     "• zeros\n"
     "• y-intercept\n"
     "• signs\n"
     "• asymptotes\n"
     "• monotonicity\n"
     "• symmetry\n"
     "• end behaviour"),

    ("Functions & Graphs", 2,
     "How do I find an inverse function?",
     "1. Write y = f(x).\n"
     "2. Swap x and y.\n"
     "3. Solve for y.\n\n"
     "The graph reflects in y=x.\n"
     "Domain and range swap."),

    ("Functions & Graphs", 3,
     "When does a function have an inverse?",
     "When it is one-to-one on the stated domain.\n\n"
     "Monotonicity is often the easiest way to show this."),


    # =========================
    # LOGS / EXPONENTS
    # =========================

    ("Logs & Exponents", 3,
     "State the main exponent laws.",
     "a^m a^n = a^(m+n)\n\n"
     "a^m / a^n = a^(m-n)\n\n"
     "(a^m)^n = a^(mn)\n\n"
     "a^(-n) = 1/a^n\n\n"
     "a^0 = 1"),

    ("Logs & Exponents", 3,
     "State the three main log laws.",
     "log(ab) = log a + log b\n\n"
     "log(a/b) = log a - log b\n\n"
     "log(a^k) = k log a"),

    ("Logs & Exponents", 3,
     "What is the domain condition for log(f(x))?",
     "f(x) > 0\n\n"
     "NOT merely f(x) ≠ 0."),

    ("Logs & Exponents", 2,
     "If a^f(x) = a^g(x), when can I equate the powers?",
     "If a > 0 and a ≠ 1:\n\n"
     "f(x) = g(x)."),

    ("Logs & Exponents", 2,
     "If log_a(f(x)) = log_a(g(x)), what can I do?",
     "Set f(x)=g(x), BUT first impose:\n\n"
     "f(x) > 0\n"
     "g(x) > 0"),

    ("Logs & Exponents", 2,
     "Change of base formula?",
     "log_a(b) = ln(b) / ln(a)"),

    ("Logs & Exponents", 3,
     "I see a^(2x) and a^x in the same equation. What substitution?",
     "Let\n\n"
     "u = a^x.\n\n"
     "Then a^(2x)=u^2.\n\n"
     "Solve the quadratic in u, remembering u > 0."),


    # =========================
    # NUMBER THEORY
    # =========================

    ("Number Theory", 3,
     "If n = p1^a1 p2^a2 ... pr^ar, how many positive divisors does n have?",
     "(a1+1)(a2+1)...(ar+1)"),

    ("Number Theory", 3,
     "A number has exactly 12 positive divisors. Possible exponent patterns?",
     "Because\n"
     "12 = 12 = 6×2 = 4×3 = 3×2×2,\n\n"
     "the possibilities are:\n\n"
     "p^11\n"
     "p^5 q\n"
     "p^3 q^2\n"
     "p^2 q r"),

    ("Number Theory", 3,
     "Prime factorisation condition for a perfect square?",
     "Every prime exponent must be EVEN."),

    ("Number Theory", 3,
     "Prime factorisation condition for a perfect cube?",
     "Every prime exponent must be a multiple of 3."),

    ("Number Theory", 3,
     "How do gcd and lcm use prime exponents?",
     "gcd → take the MINIMUM exponent.\n\n"
     "lcm → take the MAXIMUM exponent."),

    ("Number Theory", 3,
     "Relationship between gcd(a,b), lcm(a,b), a and b?",
     "For positive a,b:\n\n"
     "gcd(a,b) × lcm(a,b) = ab"),

    ("Number Theory", 3,
     "How might I handle a huge power modulo m?",
     "Find the cycle of powers modulo m.\n\n"
     "Then reduce the exponent according to the cycle length."),

    ("Number Theory", 3,
     "Possible square residues mod 4?",
     "0 or 1."),

    ("Number Theory", 2,
     "Possible square residues mod 3?",
     "0 or 1."),

    ("Number Theory", 2,
     "What is every odd square modulo 8?",
     "1 mod 8."),

    ("Number Theory", 3,
     "Prime p divides ab. What follows?",
     "p divides a OR p divides b.\n\n"
     "This is Euclid's lemma and relies on p being prime."),

    ("Number Theory", 3,
     "An integer equation becomes AB = N. What should I do?",
     "Enumerate divisor pairs of N.\n\n"
     "Then impose:\n"
     "• sign\n"
     "• parity\n"
     "• bounds\n"
     "• positivity\n\n"
     "Remember negative factor pairs if allowed."),

    ("Number Theory", 2,
     "If d divides A and d divides B, what else does d divide?",
     "Any integer linear combination:\n\n"
     "mA + nB."),

    ("Number Theory", 3,
     "Useful parity facts?",
     "even ± even = even\n"
     "odd ± odd = even\n"
     "even × anything = even\n"
     "odd × odd = odd"),


    # =========================
    # COMBINATORICS
    # =========================

    ("Combinatorics", 3,
     "Choose r objects from n, where order does NOT matter.",
     "nCr = n! / (r!(n-r)!)"),

    ("Combinatorics", 3,
     "Useful symmetry of combinations?",
     "nCr = nC(n-r)"),

    ("Combinatorics", 3,
     "Arrange n distinct objects.",
     "n!"),

    ("Combinatorics", 3,
     "Arrange repeated objects, e.g. AABBCC?",
     "If there are n objects total with repeats a,b,c,...:\n\n"
     "n! / (a! b! c! ...)"),

    ("Combinatorics", 3,
     "Choose k numbers from 1,...,n with NO two consecutive. Formula?",
     "C(n-k+1, k)\n\n"
     "This comes from removing the compulsory gaps."),

    ("Combinatorics", 3,
     "Why does the non-consecutive selection formula work?",
     "If\n"
     "x1 < x2 < ... < xk\n"
     "with gaps of at least 1,\n\n"
     "set:\n"
     "yi = xi - (i-1).\n\n"
     "Then choose k ordinary values from 1,...,n-k+1."),

    ("Combinatorics", 3,
     "Number of non-negative integer solutions to x1+...+xk=n?",
     "Stars and bars:\n\n"
     "C(n+k-1, k-1)"),

    ("Combinatorics", 3,
     "Number of POSITIVE integer solutions to x1+...+xk=n?",
     "Give each variable 1 first.\n\n"
     "Answer:\n"
     "C(n-1, k-1)"),

    ("Combinatorics", 3,
     "A counting problem says 'at least one'. What method should I consider first?",
     "The complement.\n\n"
     "Count:\n"
     "total - none"),

    ("Combinatorics", 3,
     "Two sets A and B overlap. Inclusion-exclusion formula?",
     "|A ∪ B| = |A| + |B| - |A ∩ B|"),

    ("Combinatorics", 3,
     "I need objects to be separated. What might the gaps method look like?",
     "Arrange the OTHER objects first.\n\n"
     "Then place the special objects into the gaps between / around them."),

    ("Combinatorics", 2,
     "Number of grid routes using r right steps and u up steps?",
     "Choose which steps are right (or up):\n\n"
     "C(r+u, r) = C(r+u, u)"),

    ("Combinatorics", 2,
     "A lattice path must not cross a diagonal. What structure might appear?",
     "Reflection principle / Catalan-number style counting.\n\n"
     "Do not automatically count paths individually."),

    ("Combinatorics", 3,
     "State the pigeonhole principle in a useful numerical form.",
     "If N objects are put into k boxes,\n"
     "some box contains at least\n\n"
     "ceil(N/k)\n\n"
     "objects."),

    ("Combinatorics", 3,
     "Counting feels horribly messy. Three questions I should ask?",
     "Can I:\n\n"
     "1. count the complement?\n"
     "2. encode the objects differently?\n"
     "3. create a bijection to something easier?"),


    # =========================
    # PROBABILITY
    # =========================

    ("Probability", 3,
     "For equally likely outcomes, how do I calculate P(A)?",
     "P(A) = number of favourable outcomes / total outcomes."),

    ("Probability", 3,
     "Formula for P(A ∪ B)?",
     "P(A ∪ B)\n"
     "= P(A) + P(B) - P(A ∩ B)"),

    ("Probability", 3,
     "What equation holds for independent events A and B?",
     "P(A ∩ B) = P(A)P(B)"),

    ("Probability", 3,
     "Conditional probability formula?",
     "P(A | B) = P(A ∩ B) / P(B)"),

    ("Probability", 3,
     "Probability of 'at least one' — usual shortcut?",
     "1 - P(none)"),

    ("Probability", 2,
     "What changes when sampling WITHOUT replacement?",
     "Probabilities change after each selection.\n\n"
     "The events are generally NOT independent."),

    ("Probability", 2,
     "Choose r numbers uniformly from n, unordered. Size of sample space?",
     "C(n,r), not n^r."),


    # =========================
    # SEQUENCES
    # =========================

    ("Sequences & Recurrences", 3,
     "Arithmetic sequence nth term?",
     "u_n = u_1 + (n-1)d"),

    ("Sequences & Recurrences", 3,
     "Arithmetic series sum?",
     "S_n = n/2 × [2u_1 + (n-1)d]\n\n"
     "or\n\n"
     "S_n = n/2 × (first + last)"),

    ("Sequences & Recurrences", 3,
     "Geometric sequence nth term?",
     "u_n = u_1 r^(n-1)"),

    ("Sequences & Recurrences", 3,
     "Finite geometric series sum?",
     "S_n = u_1(1-r^n)/(1-r)\n\n"
     "for r ≠ 1."),

    ("Sequences & Recurrences", 3,
     "Infinite geometric series sum?",
     "If |r| < 1:\n\n"
     "S_∞ = u_1/(1-r)"),

    ("Sequences & Recurrences", 3,
     "Recurrence u_(n+1) = r u_n + c. Best transformation?",
     "Find the fixed point L:\n\n"
     "L = rL + c.\n\n"
     "Then set\n"
     "v_n = u_n - L.\n\n"
     "Now:\n"
     "v_(n+1) = r v_n."),

    ("Sequences & Recurrences", 3,
     "Recurrence contains u_n/(1 + c u_n). What substitution should I consider?",
     "Try the reciprocal:\n\n"
     "v_n = 1/u_n."),

    ("Sequences & Recurrences", 3,
     "A recurrence contains a forcing term like 2^n or 3^n. Possible trick?",
     "Divide by that exponential.\n\n"
     "For example try:\n"
     "v_n = u_n / 2^n."),

    ("Sequences & Recurrences", 3,
     "I see 1/[n(n+1)] inside a sum. Trigger?",
     "Partial fractions:\n\n"
     "1/[n(n+1)] = 1/n - 1/(n+1).\n\n"
     "This telescopes."),

    ("Sequences & Recurrences", 3,
     "I see 1/(√(n+1)+√n) inside a sum. Trigger?",
     "Rationalise:\n\n"
     "1/(√(n+1)+√n)\n"
     "= √(n+1) - √n.\n\n"
     "Then the sum telescopes."),

    ("Sequences & Recurrences", 3,
     "Each sequence step changes by between a and b. What can I say after r steps?",
     "Total change lies between\n\n"
     "ar and br.\n\n"
     "Use global bounds instead of tracking every possible term."),

    ("Sequences & Recurrences", 2,
     "A recurrence behaves strangely with integers. What should I check before finding a closed form?",
     "Compute a few terms and look for:\n\n"
     "• periodicity\n"
     "• parity\n"
     "• modular patterns\n"
     "• invariants"),


    # =========================
    # TRIG
    # =========================

    ("Trigonometry", 3,
     "Fundamental Pythagorean trig identity?",
     "sin^2(x) + cos^2(x) = 1"),

    ("Trigonometry", 3,
     "Definition of tan(x)?",
     "tan(x) = sin(x) / cos(x)"),

    ("Trigonometry", 3,
     "Identity involving tan^2(x) and sec^2(x)?",
     "1 + tan^2(x) = sec^2(x)"),

    ("Trigonometry", 3,
     "Complementary-angle identities?",
     "sin(90° - x) = cos(x)\n\n"
     "cos(90° - x) = sin(x)"),

    ("Trigonometry", 3,
     "Trig functions of negative angles?",
     "sin(-x) = -sin(x)\n\n"
     "cos(-x) = cos(x)\n\n"
     "tan(-x) = -tan(x)"),

    ("Trigonometry", 3,
     "Periods of sin, cos and tan?",
     "sin and cos:\n"
     "360° or 2π\n\n"
     "tan:\n"
     "180° or π"),

    ("Trigonometry", 3,
     "Double-angle formula for sine?",
     "sin(2x) = 2 sin(x) cos(x)"),

    ("Trigonometry", 3,
     "Three forms of the double-angle formula for cos(2x)?",
     "cos(2x)\n"
     "= cos^2(x) - sin^2(x)\n"
     "= 2cos^2(x) - 1\n"
     "= 1 - 2sin^2(x)"),

    ("Trigonometry", 3,
     "Power-reduction formulas for sin^2(x) and cos^2(x)?",
     "sin^2(x) = [1 - cos(2x)]/2\n\n"
     "cos^2(x) = [1 + cos(2x)]/2"),

    ("Trigonometry", 3,
     "Trig equation contains both sin^2(x) and cos^2(x). First thought?",
     "Convert everything to ONE trig function using:\n\n"
     "sin^2(x) + cos^2(x) = 1."),

    ("Trigonometry", 3,
     "Trig equation factorises. What must I remember?",
     "Use the zero-product rule and solve EVERY factor.\n\n"
     "Example:\n"
     "sin(x)(2cos(x)-1)=0\n\n"
     "means solve sin(x)=0 AND 2cos(x)-1=0."),

    ("Trigonometry", 3,
     "Can I divide a trig equation by sin(x) or cos(x)?",
     "Not immediately.\n\n"
     "First consider the case where the expression you are dividing by equals zero.\n\n"
     "Otherwise you may LOSE solutions."),

    ("Trigonometry", 3,
     "Signs of trig functions by quadrant?",
     "Quadrant I: all positive\n"
     "Quadrant II: sin positive\n"
     "Quadrant III: tan positive\n"
     "Quadrant IV: cos positive"),

    ("Trigonometry", 3,
     "Range of sin(x) and cos(x)?",
     "-1 ≤ sin(x) ≤ 1\n"
     "-1 ≤ cos(x) ≤ 1\n\n"
     "Excellent for existence and bounding arguments."),

    ("Trigonometry", 3,
     "Exact trig values at 30°?",
     "sin 30° = 1/2\n\n"
     "cos 30° = √3/2\n\n"
     "tan 30° = 1/√3"),

    ("Trigonometry", 3,
     "Exact trig values at 45°?",
     "sin 45° = 1/√2\n\n"
     "cos 45° = 1/√2\n\n"
     "tan 45° = 1"),

    ("Trigonometry", 3,
     "Exact trig values at 60°?",
     "sin 60° = √3/2\n\n"
     "cos 60° = 1/2\n\n"
     "tan 60° = √3"),

    ("Trigonometry", 2,
     "Maximum possible value of |a sin x + b cos x|?",
     "√(a^2 + b^2)\n\n"
     "Think of rewriting as R sin(x+α)."),

    ("Trigonometry", 3,
     "For y = a sin(bx+c)+d, amplitude and period?",
     "Amplitude = |a|\n\n"
     "Period = 2π/|b|\n\n"
     "Midline = y=d"),

    ("Trigonometry", 2,
     "For y = a tan(bx), what is the period?",
     "π/|b|"),

    ("Trigonometry", 3,
     "General solutions of sin x = sin α?",
     "x = α + 360°n\n\n"
     "OR\n\n"
     "x = 180° - α + 360°n"),

    ("Trigonometry", 3,
     "General solutions of cos x = cos α?",
     "x = ±α + 360°n"),

    ("Trigonometry", 3,
     "General solutions of tan x = tan α?",
     "x = α + 180°n"),


    # =========================
    # GEOMETRY
    # =========================

    ("Geometry", 3,
     "Pythagoras' theorem?",
     "For a right triangle:\n\n"
     "a^2 + b^2 = c^2\n\n"
     "where c is the hypotenuse."),

    ("Geometry", 3,
     "Similar shapes have side scale factor k. What happens to area and volume?",
     "Area scale factor = k^2\n\n"
     "Volume scale factor = k^3"),

    ("Geometry", 3,
     "Main ways to prove triangles are similar?",
     "AA\n\n"
     "SAS with proportional sides\n\n"
     "SSS with proportional sides\n\n"
     "AA is usually the quickest."),

    ("Geometry", 3,
     "Once I spot similar triangles, what should I look for?",
     "Corresponding side RATIOS.\n\n"
     "Often an ugly unknown cancels when ratios are used."),

    ("Geometry", 3,
     "Area of a triangle using two sides and the included angle?",
     "Area = 1/2 ab sin(C)"),

    ("Geometry", 3,
     "Sine rule?",
     "a/sin(A) = b/sin(B) = c/sin(C)\n\n"
     "Each side pairs with its opposite angle."),

    ("Geometry", 3,
     "Cosine rule?",
     "c^2 = a^2 + b^2 - 2ab cos(C)\n\n"
     "Think of it as Pythagoras with a correction term."),

    ("Geometry", 3,
     "When should I think cosine rule?",
     "SAS or SSS.\n\n"
     "Especially when there is NOT an obvious opposite side-angle pair."),

    ("Geometry", 3,
     "When should I think sine rule?",
     "When you know an opposite side-angle pair."),

    ("Geometry", 2,
     "I draw a median or altitude. What new structures should I check for?",
     "• right triangles\n"
     "• equal lengths\n"
     "• similar triangles\n"
     "• symmetry"),

    ("Geometry", 2,
     "Two triangles share the same altitude. How do their areas compare?",
     "Their areas are proportional to their BASES."),

    ("Geometry", 2,
     "Two triangles share the same base. How do their areas compare?",
     "Their areas are proportional to their perpendicular HEIGHTS."),

    ("Geometry", 3,
     "A geometry problem has lots of lengths but absolute scale should not matter. What trick?",
     "Use similarity or choose a convenient scale.\n\n"
     "For example, set one important length equal to 1."),


    # =========================
    # CIRCLE GEOMETRY
    # =========================

    ("Circle Geometry", 3,
     "Angle at the centre vs angle at the circumference on the same arc?",
     "Angle at centre = 2 × angle at circumference."),

    ("Circle Geometry", 3,
     "Angles subtended by the same chord in the same segment?",
     "They are equal."),

    ("Circle Geometry", 3,
     "Opposite angles of a cyclic quadrilateral?",
     "They sum to 180°."),

    ("Circle Geometry", 3,
     "Relationship between a radius and a tangent at the point of contact?",
     "They are perpendicular.\n\n"
     "Angle = 90°."),

    ("Circle Geometry", 3,
     "Two tangents are drawn from the same external point. What is true?",
     "The tangent lengths are equal."),

    ("Circle Geometry", 3,
     "Angle in a semicircle?",
     "90°."),

    ("Circle Geometry", 2,
     "State the tangent-chord theorem.",
     "The angle between a tangent and a chord equals the angle in the alternate segment subtended by that chord."),

    ("Circle Geometry", 3,
     "Power of a point: tangent version?",
     "If PT is tangent from P:\n\n"
     "Power of P = PT^2."),

    ("Circle Geometry", 3,
     "Power of a point: secant version?",
     "If a secant from P meets the circle at A and B:\n\n"
     "Power of P = PA × PB.\n\n"
     "Hence often:\n"
     "PA×PB = PC×PD."),

    ("Circle Geometry", 2,
     "A line from the centre is perpendicular to a chord. What does it do?",
     "It bisects the chord."),


    # =========================
    # COORDINATE GEOMETRY
    # =========================

    ("Coordinate Geometry", 3,
     "Gradient between (x1,y1) and (x2,y2)?",
     "m = (y2-y1)/(x2-x1)"),

    ("Coordinate Geometry", 3,
     "Condition for perpendicular lines with finite non-zero gradients?",
     "m1 × m2 = -1"),

    ("Coordinate Geometry", 3,
     "Equation of a line through (x1,y1) with gradient m?",
     "y - y1 = m(x - x1)"),

    ("Coordinate Geometry", 3,
     "Distance between (x1,y1) and (x2,y2)?",
     "√[(x2-x1)^2 + (y2-y1)^2]"),

    ("Coordinate Geometry", 3,
     "Midpoint of (x1,y1) and (x2,y2)?",
     "((x1+x2)/2, (y1+y2)/2)"),

    ("Coordinate Geometry", 3,
     "Equation of circle with centre (a,b) and radius r?",
     "(x-a)^2 + (y-b)^2 = r^2"),

    ("Coordinate Geometry", 3,
     "Fast way to find the tangent gradient to a circle at point P?",
     "The radius CP is perpendicular to the tangent.\n\n"
     "Find the radius gradient and take its negative reciprocal."),

    ("Coordinate Geometry", 2,
     "Locus of points equidistant from A and B?",
     "The perpendicular bisector of AB."),

    ("Coordinate Geometry", 3,
     "Shortest distance from a point to a line or smooth curve: geometric trigger?",
     "PERPENDICULAR.\n\n"
     "For a smooth curve, the line to the nearest point is normal to the tangent."),


    # =========================
    # RADIANS
    # =========================

    ("Radians & Sectors", 3,
     "180° in radians?",
     "π"),

    ("Radians & Sectors", 3,
     "Arc length formula when θ is in radians?",
     "s = rθ"),

    ("Radians & Sectors", 3,
     "Sector area when θ is in radians?",
     "A = 1/2 r^2 θ"),

    ("Radians & Sectors", 2,
     "Chord length for radius r and central angle θ?",
     "Split into two right triangles:\n\n"
     "Chord = 2r sin(θ/2)"),

    ("Radians & Sectors", 2,
     "Area of a circular segment with central angle θ radians?",
     "Sector - triangle:\n\n"
     "1/2 r^2(θ - sin θ)"),


    # =========================
    # CALCULUS
    # =========================

    ("Calculus", 3,
     "What does f'(x) > 0 mean?",
     "f is increasing."),

    ("Calculus", 3,
     "What does f'(x) < 0 mean?",
     "f is decreasing."),

    ("Calculus", 3,
     "Necessary condition for a differentiable stationary point?",
     "f'(x) = 0"),

    ("Calculus", 3,
     "Does f'(x)=0 automatically mean maximum or minimum?",
     "NO.\n\n"
     "It could also be a stationary point of inflection."),

    ("Calculus", 3,
     "Second derivative test for a stationary point?",
     "At a stationary point:\n\n"
     "f'' > 0 → local minimum\n"
     "f'' < 0 → local maximum\n"
     "f'' = 0 → inconclusive"),

    ("Calculus", 3,
     "Optimisation on a CLOSED interval. What points must I check?",
     "Stationary points AND endpoints."),

    ("Calculus", 3,
     "Gradient of tangent to y=f(x) at x=a?",
     "f'(a)"),

    ("Calculus", 3,
     "Equation of tangent to y=f(x) at x=a?",
     "y - f(a) = f'(a)(x-a)"),

    ("Calculus", 3,
     "Gradient of normal to a curve?",
     "-1/f'(a)\n\n"
     "provided f'(a) is finite and non-zero."),

    ("Calculus", 3,
     "What does ∫ from a to b of f(x) dx represent?",
     "SIGNED area.\n\n"
     "Area below the x-axis contributes negatively."),

    ("Calculus", 3,
     "What happens when I reverse integration limits?",
     "∫a→b f(x) dx = - ∫b→a f(x) dx"),

    ("Calculus", 3,
     "How can I split an integral at c?",
     "∫a→b f = ∫a→c f + ∫c→b f"),

    ("Calculus", 3,
     "Integral of an odd function over [-a,a]?",
     "0"),

    ("Calculus", 3,
     "Integral of an even function over [-a,a]?",
     "2 × ∫0→a f(x) dx"),

    ("Calculus", 3,
     "If ∫a→b f(x) dx = 0, must f(x)=0?",
     "NO.\n\n"
     "Positive and negative signed areas can cancel."),

    ("Calculus", 3,
     "Useful inequality involving ∫f and ∫|f|?",
     "|∫a→b f(x) dx| ≤ ∫a→b |f(x)| dx"),

    ("Calculus", 3,
     "Area between curves f(x) and g(x)?",
     "Integrate |f(x)-g(x)|.\n\n"
     "Usually find their intersections and split the integral where necessary."),

    ("Calculus", 3,
     "If f(x) ≥ g(x) for every x in [a,b], compare their integrals.",
     "∫a→b f(x) dx ≥ ∫a→b g(x) dx"),

    ("Calculus", 3,
     "How should I integrate |f(x)|?",
     "Find the zeros of f.\n\n"
     "Split the interval there and reverse the sign where f is negative."),

    ("Calculus", 2,
     "Integral looks like f'(x)[f(x)]^n. Trigger?",
     "Reverse chain rule / substitution.\n\n"
     "Let u = f(x)."),

    ("Calculus", 2,
     "Integral of (ax+b)^n?",
     "(ax+b)^(n+1) / [a(n+1)] + C\n\n"
     "for n ≠ -1."),

    ("Calculus", 2,
     "Integral of f'(x)/f(x)?",
     "ln|f(x)| + C"),


    # =========================
    # LOGIC / PAPER 2
    # =========================

    ("Logic & Paper 2", 3,
     "A statement says 'for all x...'. What should I try before proving it?",
     "Try to DESTROY it with one counterexample."),

    ("Logic & Paper 2", 3,
     "Good simple counterexamples to test first?",
     "Try:\n\n"
     "0\n"
     "1\n"
     "-1\n"
     "constant functions\n"
     "linear functions\n"
     "equality cases\n"
     "extreme values"),

    ("Logic & Paper 2", 3,
     "How do I disprove P → Q?",
     "Find ONE example where:\n\n"
     "P is true\n"
     "but\n"
     "Q is false."),

    ("Logic & Paper 2", 3,
     "Contrapositive of P → Q?",
     "NOT Q → NOT P\n\n"
     "The contrapositive is logically equivalent to the original statement."),

    ("Logic & Paper 2", 3,
     "Converse of P → Q?",
     "Q → P\n\n"
     "It is NOT automatically equivalent to the original."),

    ("Logic & Paper 2", 3,
     "'P is sufficient for Q' means what?",
     "P → Q"),

    ("Logic & Paper 2", 3,
     "'P is necessary for Q' means what?",
     "Q → P"),

    ("Logic & Paper 2", 3,
     "Negation of: 'For all x, P(x)'?",
     "There exists an x for which P(x) is false.\n\n"
     "¬(∀x P(x)) ↔ ∃x ¬P(x)"),

    ("Logic & Paper 2", 3,
     "Negation of: 'There exists x such that P(x)'?",
     "For every x, P(x) is false.\n\n"
     "¬(∃x P(x)) ↔ ∀x ¬P(x)"),

    ("Logic & Paper 2", 3,
     "What must be shown for P if and only if Q?",
     "Both directions:\n\n"
     "P → Q\n"
     "AND\n"
     "Q → P"),

    ("Logic & Paper 2", 3,
     "A graph makes a statement look obviously true. What should I do?",
     "Translate the picture into an exact inequality or implication.\n\n"
     "Then test the actual statement.\n\n"
     "Do not trust the sketch alone."),


    # =========================
    # META TECHNIQUES
    # =========================

    ("TMUA Strategy", 3,
     "I see a horrible algebraic expression. First question?",
     "Can I CHANGE REPRESENTATION?\n\n"
     "Try:\n"
     "• factorisation\n"
     "• substitution\n"
     "• graph\n"
     "• symmetry\n"
     "• ratios\n"
     "• modular arithmetic"),

    ("TMUA Strategy", 3,
     "A problem gives integer restrictions. What mindset should I switch into?",
     "Think:\n\n"
     "• divisibility\n"
     "• parity\n"
     "• modular arithmetic\n"
     "• factor pairs\n"
     "• prime factorisation\n\n"
     "Don't automatically solve over the reals first."),

    ("TMUA Strategy", 3,
     "Question asks HOW MANY solutions. What techniques should come to mind?",
     "Think:\n\n"
     "• graphs / intersections\n"
     "• discriminant\n"
     "• monotonicity\n"
     "• turning points\n"
     "• tangency\n\n"
     "You often don't need to explicitly solve."),

    ("TMUA Strategy", 3,
     "Variables appear symmetrically. What substitutions might help?",
     "Try:\n\n"
     "x+y\n"
     "xy\n"
     "x-y\n"
     "or exploit the ability to swap x and y."),

    ("TMUA Strategy", 3,
     "I see both x and 1/x. What should I consider?",
     "Try:\n\n"
     "• multiplying through by x\n"
     "• u = x + 1/x\n"
     "• reciprocal symmetry"),

    ("TMUA Strategy", 3,
     "There seem to be loads of cases. Before case-bashing, what should I search for?",
     "A:\n\n"
     "• bound\n"
     "• invariant\n"
     "• parity restriction\n"
     "• symmetry\n"
     "• monotonicity argument"),

    ("TMUA Strategy", 3,
     "Geometry problem has no obvious route. What order of ideas should I hunt for?",
     "Try:\n\n"
     "1. similar triangles\n"
     "2. circle / cyclic quadrilateral\n"
     "3. Pythagoras\n"
     "4. auxiliary line\n"
     "5. coordinates"),

    ("TMUA Strategy", 3,
     "Trig equation looks horrible. What is the general rescue strategy?",
     "1. Rewrite in ONE trig function if possible.\n"
     "2. Use identities.\n"
     "3. Factor.\n"
     "4. Solve each factor.\n"
     "5. Check the required interval.\n\n"
     "Never divide away zero solutions."),

    ("TMUA Strategy", 3,
     "In multiple choice, do I need a full textbook-style solution?",
     "NO.\n\n"
     "Use the answer options.\n\n"
     "Try:\n"
     "• substitution\n"
     "• parity\n"
     "• signs\n"
     "• bounds\n"
     "• elimination\n"
     "• special cases"),

    ("TMUA Strategy", 3,
     "I've done algebra for ages and the expression is getting WORSE. What should that signal?",
     "STOP.\n\n"
     "TMUA probably wants structure rather than expansion.\n\n"
     "Look for:\n"
     "factorisation, graph, symmetry, substitution, bounds, or a counterexample."),

]


# ============================================================
# GUI
# ============================================================

class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("TMUA Flashcards")
        self.root.geometry("1100x760")
        self.root.minsize(850, 600)

        self.category_var = tk.StringVar(value="All")
        self.priority_only_var = tk.BooleanVar(value=False)

        self.deck = []
        self.index = 0
        self.showing_back = False

        self.setup_style()
        self.build_gui()
        self.rebuild_deck()

        # Keyboard shortcuts
        self.root.bind("<space>", self.flip_card)
        self.root.bind("<Right>", self.next_card)
        self.root.bind("<Left>", self.previous_card)
        self.root.bind("s", self.shuffle_deck)
        self.root.bind("S", self.shuffle_deck)

    def setup_style(self):
        style = ttk.Style()

        try:
            style.theme_use("clam")
        except tk.TclError:
            pass

        style.configure(
            "Big.TButton",
            font=("Helvetica", 13),
            padding=10
        )

        style.configure(
            "Top.TLabel",
            font=("Helvetica", 12)
        )

    def build_gui(self):

        # ---------------- TOP CONTROLS ----------------
        top_frame = ttk.Frame(self.root, padding=15)
        top_frame.pack(fill="x")

        ttk.Label(
            top_frame,
            text="Category:",
            style="Top.TLabel"
        ).pack(side="left", padx=(0, 8))

        categories = sorted(set(card[0] for card in CARDS))
        categories.insert(0, "All")

        self.category_box = ttk.Combobox(
            top_frame,
            textvariable=self.category_var,
            values=categories,
            state="readonly",
            width=24,
            font=("Helvetica", 11)
        )
        self.category_box.pack(side="left", padx=(0, 15))
        self.category_box.bind(
            "<<ComboboxSelected>>",
            lambda event: self.rebuild_deck()
        )

        priority_check = ttk.Checkbutton(
            top_frame,
            text="★★★ only",
            variable=self.priority_only_var,
            command=self.rebuild_deck
        )
        priority_check.pack(side="left")

        self.count_label = ttk.Label(
            top_frame,
            text="",
            style="Top.TLabel"
        )
        self.count_label.pack(side="right")

        # ---------------- CARD AREA ----------------
        card_outer = ttk.Frame(self.root, padding=(40, 20))
        card_outer.pack(fill="both", expand=True)

        self.card_frame = tk.Frame(
            card_outer,
            bg="#ffffff",
            highlightbackground="#bbbbbb",
            highlightthickness=2
        )
        self.card_frame.pack(fill="both", expand=True)

        self.side_label = tk.Label(
            self.card_frame,
            text="FRONT",
            bg="#ffffff",
            fg="#666666",
            font=("Helvetica", 12, "bold")
        )
        self.side_label.pack(pady=(30, 5))

        self.category_label = tk.Label(
            self.card_frame,
            text="",
            bg="#ffffff",
            fg="#555555",
            font=("Helvetica", 11)
        )
        self.category_label.pack(pady=(0, 10))

        self.priority_label = tk.Label(
            self.card_frame,
            text="",
            bg="#ffffff",
            fg="#333333",
            font=("Helvetica", 14)
        )
        self.priority_label.pack()

        self.card_text = tk.Label(
            self.card_frame,
            text="",
            bg="#ffffff",
            fg="#111111",
            font=("Helvetica", 20),
            justify="center",
            wraplength=850
        )
        self.card_text.pack(
            fill="both",
            expand=True,
            padx=50,
            pady=30
        )

        # Click card to flip
        self.card_frame.bind("<Button-1>", self.flip_card)
        self.card_text.bind("<Button-1>", self.flip_card)
        self.side_label.bind("<Button-1>", self.flip_card)

        # ---------------- BUTTONS ----------------
        button_frame = ttk.Frame(self.root, padding=(20, 5, 20, 20))
        button_frame.pack(fill="x")

        ttk.Button(
            button_frame,
            text="← Previous",
            style="Big.TButton",
            command=self.previous_card
        ).pack(side="left", padx=5)

        ttk.Button(
            button_frame,
            text="Shuffle",
            style="Big.TButton",
            command=self.shuffle_deck
        ).pack(side="left", padx=5)

        self.flip_button = ttk.Button(
            button_frame,
            text="Flip Card",
            style="Big.TButton",
            command=self.flip_card
        )
        self.flip_button.pack(side="left", expand=True, padx=20)

        ttk.Button(
            button_frame,
            text="Next →",
            style="Big.TButton",
            command=self.next_card
        ).pack(side="right", padx=5)

        # ---------------- SHORTCUT INFO ----------------
        shortcut_label = ttk.Label(
            self.root,
            text="Space = flip     ← / → = previous / next     S = shuffle     Click card = flip",
            foreground="#666666",
            font=("Helvetica", 10)
        )
        shortcut_label.pack(pady=(0, 12))

    def rebuild_deck(self):
        selected_category = self.category_var.get()

        self.deck = []

        for card in CARDS:
            category, priority, front, back = card

            category_ok = (
                selected_category == "All"
                or category == selected_category
            )

            priority_ok = (
                not self.priority_only_var.get()
                or priority == 3
            )

            if category_ok and priority_ok:
                self.deck.append(card)

        random.shuffle(self.deck)

        self.index = 0
        self.showing_back = False

        self.display_card()

    def display_card(self):
        if not self.deck:
            self.side_label.config(text="")
            self.category_label.config(text="")
            self.priority_label.config(text="")
            self.card_text.config(text="No flashcards match this filter.")
            self.count_label.config(text="0 cards")
            return

        category, priority, front, back = self.deck[self.index]

        stars = "★" * priority + "☆" * (3 - priority)

        self.category_label.config(text=category)
        self.priority_label.config(text=stars)

        if self.showing_back:
            self.side_label.config(
                text="BACK",
                fg="#356859"
            )
            self.card_text.config(text=back)
            self.flip_button.config(text="Show Front")
        else:
            self.side_label.config(
                text="FRONT",
                fg="#76528b"
            )
            self.card_text.config(text=front)
            self.flip_button.config(text="Flip Card")

        self.count_label.config(
            text=f"{self.index + 1} / {len(self.deck)}"
        )

    def flip_card(self, event=None):
        if not self.deck:
            return

        self.showing_back = not self.showing_back
        self.display_card()

    def next_card(self, event=None):
        if not self.deck:
            return

        self.index = (self.index + 1) % len(self.deck)
        self.showing_back = False
        self.display_card()

    def previous_card(self, event=None):
        if not self.deck:
            return

        self.index = (self.index - 1) % len(self.deck)
        self.showing_back = False
        self.display_card()

    def shuffle_deck(self, event=None):
        if not self.deck:
            return

        random.shuffle(self.deck)
        self.index = 0
        self.showing_back = False
        self.display_card()


# ============================================================
# START PROGRAM
# ============================================================

if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardApp(root)
    root.mainloop()