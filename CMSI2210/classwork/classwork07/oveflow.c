double magnitude(double re, double im)
{
    double r;
 
    re = fabs(re);
    im = fabs(im);
    if (re > im) {
        r = im/re;
        return re*sqrt(1.0+r*r);
    }
    if (im == 0.0)
        return 0.0;
    r = re/im;
    return im*sqrt(1.0+r*r);
}