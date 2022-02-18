#!/usr/bin/env python
# coding: utf-8

# In[1]:


def sucesorDia (dia):
    if (dia=="lunes"):
        print ("martes")
    if (dia=="martes"):
        print ("miércoles")
    if (dia=="miércoles"):
        print ("jueves")
    if (dia=="jueves"):
        print ("viernes")
    if (dia=="viernes"):
        print ("sábado")
    if (dia=="sábado"):
        print ("domingo")
    if (dia=="domingo"):
        print ("lunes")
    
sucesorDia ("martes")


# In[12]:


def clasificar (a,b):
    suma= a+b
    producto=a*b
    print (a)
    print (b)
    print (suma)
    print (producto)
    if (a>b):
        if (a>suma):
            if (a>producto):
                if (b>suma):
                    if (b>producto):
                        if (suma>producto):
                            return (producto,suma,b,a)
                        else:
                            return (suma,producto,b,a)
                    else:
                        return (suma,b,producto,a)
                else:
                    if (b>producto):
                        return (producto,b,suma,a)
                    else:
                        if (suma>producto):
                            return (b,producto,suma,a)
                        else:
                            return (b,suma,producto,a)
            else:
                if (b>suma):
                    return (suma,b,a,producto)
                else:
                    return(b,suma,a,producto)
        else:
            if (a>producto):
                if (b>producto):
                    return (producto,b,a,suma)
                else:
                    return (b,producto,a,suma)
            else:
                if (suma>producto):
                    return (b,a,producto,suma)
                else:
                    return (b,a,suma,producto)
    else:
        if (a>suma):
            if (a>producto):
                if (suma>producto):
                    return (producto,suma,a,b)
                else:
                    return (suma,producto,a,b)
            else:
                if (b>producto):
                    return (suma,a,producto,b)
                else:
                    return (suma,a,b,producto)
        else:
            if (b>suma):
                if (a>producto):
                    return (producto,a,suma,b)
                else:
                    if (suma>producto):
                        return(a,producto,suma,b)
                    else:
                        if (b>producto):
                            return (a,suma,producto,b)
                        else:
                            return (a,suma,b,producto)
            else:
                if (suma>producto):
                    if (b>producto):
                        if (a>producto):
                            return (producto,a,b,suma)
                        else:
                            return (a,producto,b,suma)
                    else:
                        return (a,b,producto,suma)
                else:
                    return (a,b,suma,producto)
                
        
clasificar (-2,9)


# In[18]:


def importe (precio):
    descuento=0
    if (precio>=100 and precio<=500):
        descuento=0.05*precio
    elif (precio>500):
        descuento= 0.08*precio
    return descuento
importe (1000)
        


# In[26]:


def calculoMedia (n1,n2,n3,n4):
    media= (n1+n2+n3+n4)/4
    if (media>15):
        return (media,"Alumno con talento")
    elif (media>=12):
        return (media, "Con capacidad")
    return (media, "Debe reorientarse")
calculoMedia (12,13,12,13)


# In[32]:


def importeDescuento (ninos):
    descuento=0
    if (ninos>4):
        descuento=18+(ninos-4)
    else:
        if (ninos==4):
            descuento=18
        if (ninos==3):
            descuento=15
        if (ninos==2):
            descuento=10
    return descuento
importeDescuento(6)


# In[37]:


def calculoDescuento (pedido,cliente):
    descuento=0
    if (pedido>40000):
        descuento=20
    else:
        if(pedido>=20001):
            descuento=15
        if (pedido>10000):
            descuento=10
    if (cliente=="COMMAQ" and descuento>0):
        descuento=descuento-2
    elif (cliente=="BEL"):
        descuento= descuento+1
    return descuento
calculoDescuento(5000,"COMMAQ")


# In[40]:


def viajeEscolar (alumnos,dias):
    costeAlumno=0
    costeGlobal=0
    if (alumnos>35):
        costeAlumno=61+3.5*dias+3.5*dias
    else:
        if (alumnos>=31):
            costeAlumno=61+3.5*dias+4*dias
        elif (alumnos>25):
            costeAlumno=61+3.5*dias+4.75*dias
        else:
            costeAlumno=67.3+3.5*dias+4.75*dias
    costeGlobal=costeAlumno*alumnos
    return (costeGlobal, costeAlumno)
viajeEscolar (33,5)


# In[4]:


def calculoPrima (accidentes,distancia,año):
    prima=distancia*0.01
    if (prima>400):
        prima=400
    if (año>=4):
        prima= prima+20*(año-4)
    if (accidentes>3):
        prima=0
    else:
        if(accidentes==3):
            prima= prima*0.25
        else:
            if(accidentes==2):
                prima= prima/3
            else:
                if (accidentes==1):
                    prima=prima/2
    return prima
calculoPrima(1,1,1)
        
        
        


# In[ ]:




