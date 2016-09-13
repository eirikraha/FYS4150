#include <iostream>     /* output */
#include "solver.h"

void general_tridiag_solver(int n, double *a, double *b, double *c, double *p, double*v)
{
    /*!
     * \brief General tridiagonal solver
     */

    /* Forward substitution */
    for (int i=1; i <= n; i++){ //n+1 instead?
        p[i] = p[i] - p[i-1]*(a[i]/b[i-1]);
        b[i] = b[i] - ((c[i-1]*a[i])/b[i-1]);
    }

    /* Backwards substitution */
    v[n] = p[n]/b[n];   /*I believe there is something wrong with my indexing*/
    for (int i=n-1; i >= 1; i--){
        v[i] = (p[i] - c[i]*v[i+1])/b[i];
    }

    return;
}

void special_tridiag_solver(int n, double *b, double *p, double *v)
{
    /*!
     * \brief Specialized tridiagonal solver for our situation
     */
    double a = -1.0, c = -1.0;

    /* Forward substitution */
    for (int i=1; i <= n; i++){ //n+1 instead?
        p[i] = p[i] - p[i-1]*(a/b[i-1]);
        b[i] = b[i] - ((c*a)/b[i-1]);
    }

    /* Backwards substitution */
    v[n] = p[n]/b[n];   /*I believe there is something wrong with my indexing*/
    for (int i=n-1; i >= 1; i--){
        v[i] = (p[i] - c*v[i+1])/b[i];
    }

    return;
}

void LU_decomp_solver(int n, double *b, double *p, double *v)
{
    /*!
     * \brief Solving via general LU-decomposition
     */
    return;
}
