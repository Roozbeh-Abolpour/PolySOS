
class Polynomial:
    def __init__(self, monomials, coefficients):
        if len(monomials)!=len(coefficients):
            raise ValueError("Monomials and coefficients must have the same length")        
        terms={}
        for m,c in zip(monomials, coefficients):
            if m in terms:
                terms[m]+=c
            else:
                terms[m]=c
        terms={m: c for m, c in terms.items() if c != 0}
        self._terms=terms 
        self.n=len(monomials[0].powers) if monomials else 0

    @property
    def degree(self):
        return max(m.degree for m in self._terms.keys()) if self._terms else 0

    @property
    def monomials(self):
        return set(self._terms.keys())
    
    @property
    def coefficients(self):
        return set(self._terms.values())    
    
    def coefficient(self, m):
        return self._terms.get(m, 0)
    
    
    @classmethod
    def from_dict(cls, terms):
        obj=cls.__new__(cls)
        obj._terms=terms
        return obj
    
    def __add__(self,other):
        if not isinstance(other, Polynomial):
            raise ValueError("Can only add another Polynomial")
        
        new_terms=self._terms.copy()
        for m,c in other._terms.items():
            if m in new_terms:
                new_terms[m]+=c
                if new_terms[m]==0:
                    del new_terms[m]
            elif c!=0:
                new_terms[m]=c  
        
        return Polynomial.from_dict(new_terms)

    def __mul__(self,other):
        if not isinstance(other,Polynomial):
            raise ValueError("Can only multiply with another Polynomial")
        new_terms={}
        for m1,c1 in self._terms.items():
            for m2,c2 in other._terms.items():                
                m=m1*m2
                if m in new_terms:
                    new_terms[m]+=c1*c2
                    if new_terms[m]==0:
                        del new_terms[m]
                elif c1*c2!=0:
                    new_terms[m]=c1*c2
        
        return Polynomial.from_dict(new_terms)



