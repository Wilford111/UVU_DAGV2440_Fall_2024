import maya.cmds as asdf

asdf.polySphere(radius=3, subdivisionsX=20, subdivisionsY=20, axis=[0,1,0], createUVs=2, constructionHistory=1)
asdf.move(0, 4.5, 0, relative=True, objectSpace=True, worldSpaceDistance=True)

asdf.polySphere(r=1, sx=20, sy=20, ax=[0,1,0], cuv=2, ch=1)
asdf.polySphere(e=True, r=2)
asdf.move(0,9,0, r=True, os=True, wd=True)

asdf.polyCylinder(r=3, sx=6, sy=1, ax=[0,1,0], cuv=3, ch=1)
asdf.move(0,1,0, r=True, os=True, wd=True)

asdf.polySphere(r=1, sx=10, sy=10, ax=[0,1,0], cuv=2, ch=1)
asdf.rotate(90,0,0, r=True, os=True, fo=True)
asdf.scale(0.314,0.314,0.314, ws=True, r=True)
asdf.move(0.537,1.881,-9.194, r=True, os=True, wd=True)
asdf.polySoftEdge(a=180, ch=1, name='pSphere3')

asdf.duplicate(rr=True)
asdf.move(-1.074,0,0, r=True, os=True, wd=True)
asdf.polySoftEdge(a=180, ch=1, name='pSphere4')

asdf.duplicate(smartTransform=True)
asdf.move(1.611,-0.931597,-0.139287, r=True)
asdf.scale(2.056911,1,1, ws=True, r=True)
asdf.scale(1,0.576155,1, ws=True, r=True)
asdf.polySoftEdge(a=180, ch=1, name='pSphere5')

# print (asdf.listRelatives('L_Arm_02_Jnt', parent=True) [0])

# txt = 'L_Arm_01_Jnt'

# txt2 = (txt.rpartition('_')[0])
# txt2 = '%s_Ctrl' %txt2
# print(txt2)