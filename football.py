import hou

parentNode: hou.Node = hou.node('/obj/grid1')
platonic: hou.Node = parentNode.createNode("platonic")
polybevel: hou.Node = parentNode.createNode("polybevel::3.0")
polyextrude: hou.Node = parentNode.createNode("polyextrude::2.0")

polyextrude.setNextInput(platonic)
polybevel.setNextInput(polyextrude)

platonic.parm("type").set(5)
polyextrude.parm("dist").set(0.092)
polyextrude.parm("splittype").set("elements")
polybevel.parm("offset").set(0.023)

polyextrude.moveToGoodPosition()
polybevel.moveToGoodPosition()
