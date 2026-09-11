# __init__ is also used to define the class and built in function used to save or hold properties of a class
import time

class MicrowaveOven:

    def __init__(self,ProductNamePV,sizePV,colorPV,bodyPV,heatingPV,cookingPV,defrostingPV,bakingPV,grillingPV,SelfFeaturingPV):
        self.ProductNameIV = ProductNamePV 
        self.sizeIV = sizePV 
        self.colorIV = colorPV          # Instance Variable (IV) = Parameter Variable (PV)
        self.bodyIV = bodyPV 
        self.heatingIV = heatingPV
        self.cookingIV = cookingPV 
        self.defrostingIV = defrostingPV 
        self.bakingIV = bakingPV 
        self.grillingIV = grillingPV
        self.SelfFeaturingIV = SelfFeaturingPV

# All the parameter variables (such as heatingPV) on the right hand side should be exactly same 
# For Example 
# self = IFB
# ProductName= "IFB Cook-Smart"
# size=10
# color="Blue"
# body="Metallic"
# These values first come to the parameters of the __init__ function and then are assigned to 
# the properties of the class using self such as 
# self.ProductName 
# self.size
# self.color 
# self.size = size 
# self.color = color 
# self.body = body 

# cooking and cook etc. which are also clear to understand
    def heat(self,item):
        if self.heatingIV == "yes":
            HeatTime = int(input("Enter the no. of seconds you want to heat:  "))
            print(f"Heating has started.Please wait while heating is in progress: ")
            i=0
            while i<=HeatTime:
                print(f"Time Remaining: {HeatTime-i} seconds")
                time.sleep(1)
                i+=1
            print(f"Heating has completed.Please take the heated {item} out of oven.")
        else:
            print("Heating cannot be done as this feature is not available :")
        
    def cook(self,item):
        if self.cookingIV == "yes":
            CookTime = int(input("Enter the no. of seconds you want to cook:  "))
            print(f"Cooking has started.Please wait while cooking is in progress: ")
            i=0
            while i<=CookTime:
                print(f"Time Remaining: {CookTime-i} seconds")
                time.sleep(1)
                i+=1
            print(f"Cooking has completed.Please take the cooked {item} out of oven.")
        else:
            print("Cooking cannot be done as this feature is not available :")
        
    def defrost(self,item):
        if self.defrostingIV == "yes":
            DefrostTime = int(input("Enter the no. of seconds you want to Defrost:  "))
            print(f"Defrosting has started.Please wait while Defrosting is in progress: ")
            i=0
            while i<=DefrostTime:
                print(f"Time Remaining: {DefrostTime-i} seconds")
                time.sleep(1)
                i+=1
            print(f"Defrosting has completed.Please take the defrosted {item} out of oven.")
        else:
            print("Defrosting cannot be done as this feature is not available :")
        
    def bake(self,item):
        if self.bakingIV == "yes":
            BakeTime = int(input("Enter the no. of seconds you want to bake:  "))
            print(f"Baking has started.Please wait while baking is in progress: ")
            i=0
            while i<=BakeTime:
                print(f"Time Remaining: {BakeTime-i} seconds")
                time.sleep(1)
                i+=1
            print(f"Baking has completed.Please take the baked {item} out of oven.")
        else:
            print("feature not available :")
        
    def grill(self,item):
        if self.grillingIV == "yes":
            GrillTime = int(input("Enter the no. of seconds you want to cook:  "))
            print(f"Grilling has started.Please wait while grilling is in progress: ")
            i=0
            while i<=GrillTime:
                print(f"Time Remaining: {GrillTime-i} seconds")
                time.sleep(1)
                i+=1
            print(f"Grilling has completed.Please take the grilled {item} out of oven.")
        else:
            print("Grilling cannot be done as this feature is not available :")
    
    def SelfFeatures(self):
        if self.SelfFeaturingIV == "yes":
            print("Selected Oven name is ",self.ProductNameIV)
            print("---------------------------------------------------------------------------------------------")
            print(f"Features of {self.ProductNameIV} are: ")
            print("---------------------------------------------------------------------------------------------")
            print(f"Size : {self.sizeIV} litres.")
            print(f"Color : {self.colorIV}.")
            print(f"Body : {self.bodyIV}.")
            print(f"Heat : {self.heatingIV}.")
            print(f"Cook : {self.cookingIV}.")
            print(f"Defrost : {self.defrostingIV}.")
            print(f"Bake : {self.bakingIV}.")
            print(f"Grill : {self.grillingIV}.")


# Creating Objects using the Class Blueprint

IFB = MicrowaveOven("IFB Cook-Smart",10,"Blue","Metallic","yes","yes","yes","yes","no","yes")
Samsung = MicrowaveOven("Samsung Insta-Cook",12,"Black","Ceramic-Metallic","yes","yes","yes","no","no","yes")
LG = MicrowaveOven("LG Easy-Cook",8,"Dark-Green","Metallic","yes","no","yes","no","no","yes")

# Program Execution Starts Here
print("---------------------------------------------------------------------------------------------")
print(f"The available microwave oven Brands are: IFB, Samsung, LG.")
print("---------------------------------------------------------------------------------------------")
print(f"The available microwave ovens are: {IFB.ProductNameIV}, {Samsung.ProductNameIV}, {LG.ProductNameIV}.")
print("---------------------------------------------------------------------------------------------")

Brand = input("Please Enter the exact name of Oven Brand which you want to try:  ")
print("---------------------------------------------------------------------------------------------")

item = input("Please Enter the name of food which you want to try: ")
print("---------------------------------------------------------------------------------------------")

match Brand:
    case "IFB":
        IFB.SelfFeatures()
        task = input("What task you want to perform: ")
        task = task.lower()
        match task:
            case "heat":
                IFB.heat(item)
            case "cook":
                IFB.cook(item)
            case "defrost":
                IFB.defrost(item)
            case "bake":
                IFB.bake(item)
            case "grill":
                IFB.grill(item)

    case "Samsung":
        Samsung.SelfFeatures()
        task = input("What task you want to perform: ")
        task = task.lower()
        match task:
            case "heat":
                Samsung.heat(item)
            case "cook":
                Samsung.cook(item)
            case "defrost":
                Samsung.defrost(item)
            case "bake":
                Samsung.bake(item)
            case "grill":
                Samsung.grill(item)

    case "LG":
        LG.SelfFeatures()
        task = input("What task you want to perform: ")
        task = task.lower()
        match task:
            case "heat":
                LG.heat(item)
            case "cook":
                LG.cook(item)
            case "defrost":
                LG.defrost(item)
            case "bake":
                LG.bake(item)
            case "grill":
                LG.grill(item)
print("---------------------------------------------------------------------------------------------")




