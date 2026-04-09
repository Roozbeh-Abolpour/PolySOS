
class Monomial:
    def __init__(self, powers):        
        self._powers = tuple(powers)        
    
    @property
    def powers(self):
        return self._powers
    
    def __str__(self):
        if self.degree==0:
            return "1"
        str=""
        for i in range(len(self._powers)):
            if self._powers[i]>1:            
                str+=f"x{i+1}^{self._powers[i]}"                
            elif self._powers[i]==1:
                str+=f"x{i+1}"
        return str
    
    def __eq__(self, other):
        if not isinstance(other, Monomial):
            return False
        return self._powers == other._powers

    def __mul__(self, other):
        if not isinstance(other, Monomial):
            raise ValueError("Can only multiply with another Monomial")
        if len(self._powers) != len(other._powers):   
            raise ValueError("Monomials must have the same number of variables")
        
        new_powers = list(self._powers)
        for i in range(len(new_powers)):
            new_powers[i] += other._powers[i]
        return Monomial(new_powers)    
    
    def __hash__(self):
        return hash(self._powers)

    def submonomials(self):
        powers=self._powers
        n=len(powers)
        x=[0]*n
        monomials=set()
        while True:
            monomials.add(Monomial(x.copy()))
            i=n-1
            while i>=0:
                x[i]+=1
                if x[i]<=powers[i]:                    
                    break
                x[i]=0
                i-=1
            if i<0:
                break            
        return monomials
    
    @property
    def degree(self):
        return sum(self._powers)
    