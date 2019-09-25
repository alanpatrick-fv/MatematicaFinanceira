def iDesc(vp, vf, n): #Descobrir a taxa do desconto racinal dados o valor liquidado, o valor nominal e o período
  return (1-(vp/vf))/n

def iJComp(t,M,C): #Descobrir a taxa composta, dados o período, o montante e o capital
  z = (((M/C)**(1/t)) - 1)*100
  return "Taxa de Juros composta é {}%".format(round(z,2))

def M(C, i, t): #Descubra o montante, dados os capital, a taxa de juros e o período
  return C*((1+(i/100))**t)
