{
   char *s = (char *) malloc (sizeof (*s));
   s[0] = 'a';
   printf ("%c", *(s + 1));
}
2.

{
   char *s = (char *) malloc (sizeof (*s) * 6);
   char *t;
   strcpy (s, "cs216");
   t = s;
   free (t);
   printf ("%s", s);
}
3.
char *select (int v, char **s)
{
   if (v) return *s;
   return 1[s];
}

int main (int argc, char **argv) 
{
   char **s = (char **) malloc (sizeof (*s) * 2);
   char *t1 = (char *) malloc (sizeof (*t1) * 6);
   char *t2 = (char *) malloc (sizeof (*t2) * 6);
   char *p;

   s[0] = t1;
   s[1] = t2;
   s[0][0] = 'b';
   p = select (0, s);
   p[0] = 'a';
   
   printf ("%c", **s);
  
}