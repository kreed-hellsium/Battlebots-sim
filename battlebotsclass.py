class battlebots:
  def __init__(self, name, metaltype, attacktype, defensetype, wheeltype, color, ):
    self.name = name
    self.metaltype = metaltype
    self.attacktype = attacktype
    self.defensetype = defensetype
    self.wheeltype = wheeltype
    self.color = color
    self.health = 0
    self.damagecoefficient = 0
    self.attacked_or_defended = "null"
    self.attack_landed_or_missed = "null"
    

  def get_name(self):
    return self.name
  def get_metaltype(self):
    return self.metaltype
  def get_attacktype(self):
    return self.attacktype
  def get_defensetype(self):
    return self.defensetype
  def get_wheeltype(self):
    return self.wheeltype
  def get_color(self):
    return self.color
  def __str__(self):
    return "%s is made with %s metal, attacks with %s, defends with %s, has %s wheels, and is %s" %(self.name, self.metaltype, self.attacktype, self.defensetype, self.wheeltype, self.color)
#metaltype comes with a durability value
    
#metal types: steel, titanium
    
#attack type: projectile, electricity, water, bash, bulldozer

#defense type: shield, rubber coating, evaporator, cross arms, chain mail

#wheeltype: small (high agility, low speed)                         medium (med agility, med speed)                        large (low agility, high speed)
################################################
