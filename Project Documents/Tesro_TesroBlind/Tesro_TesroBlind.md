# Thamees

Includes the following business units:

1. **Tesro** 
2. **Tesro Blind** 
3. **Korzo**

---

## Tesro

- **Products**: Fabric, Track 
- **Purchase**: Fabric, Track (as components) 
  - **2-step purchase**: 
    1. Vendor → Input Location 
    2. Input Location → Stock Location 
- **Manufacture**: Track 
- **Sale**: 
  - Track *(manufactured from Track components)* 
  - Fabric 
  - Track (components sale manually)

---

## Tesro Blind

- **Products**: Blind, Track, Blind Fabric 
- **Purchase**: Blind (components), Track (components), Blind Fabric
  - **2-step purchase**: 
    1. Vendor → Input Location 
    2. Input Location → Stock Location 
- **Manufacture**: Blind, Track 
- **Sale**: 
  - Blind *(manufactured from Blind components, Blind Fabric manually added at time of sale)* 
    - **Flow**: Fabric Cutting → Blind Order → Delivery 
  - Track *(manufactured from Track components)* 
    - **Flow**: Track Order → Delivery 
  - Blind and Track components (sold manually)

---

# APP: Set Delivery Info By Barcode

Using this app, you can automatically set the following fields in an invoice (under the **Other Info** tab):

- **Delivery Date** 
- **Delivered By** 
- **Delivery Entity** 
- **Delivery Salesperson**

## Select "Delivered By"

You can choose from the following delivery entities:

- Salesman 
- Driver 
- Courier 

## Invoice Barcode Format:
	Invoice1Name
	Invoice2Name
	.....
	.....
	Badge ID
	space

## Badge ID 

To get the **Badge ID**, go to: 
`Salesman/Employee > HR Settings > Badge ID`

---

# 1. APP: Barcode > Internal Transfers

- After completing Step 1 of fabric purchase, the product is stored in the **Input** location.
- In Step 2, the product should be transferred to a **Stock/Sub** location using the barcode-based **Internal Transfer** app.
- Scan Lots / Serial Numbers of products currently in the Input location 
- Scan the Stock/Sub Location barcode (destination) 
- Validate

**Transfer Flow**: 
`Input → Stock/Sub`

---

# 2.1 APP: Transfer Details

- When a **Sale Order** is created and confirmed, an **Approve** button will appear.
- On clicking the **Approve** button, a **Transfer Detail** is automatically created **if the product is not available in the Output location**.
- You must **scan or select the Lot** that you want to transfer from **Stock/Sub → Output**.
- Once scanned or selected, the system will update the transfer to move stock from **Stock/Sub → Output**.

**Transfer Flow**: 
`Stock/Sub → Output`

---

# 2.2 APP: Component Internal Transfer

- When a **Sale Order** is created and confirmed, an **Approve** button will appear.
- On clicking the **Approve** button, **if the product is not available in the Component-Output location** you need to use Component Internal Transfer.
- Scan Package name of products currently in the Stock/sub location.
- Validate.

**Transfer Flow**: 
`Stock/Sub → Component-Output`

---

# 3. APP: Cutting to Stock

- When stock is available in the **Output** location and needs to be transferred to a **Stock/Sub** location, use the **Cutting to Stock** process.
- Scan **Lot / Serial Numbers** of the product in the Output location 
- Scan the **Stock/Sub Location** barcode (destination)

**Transfer Flow**: 
`Output → Stock/Sub`

> ⚠️ Note: **Component products** do not require transfer from Component-Output → Stock/Sub.
---

# 4. APP: Stock to Stock

- One Stock/sub location To Other Stock/sub Location

---

# FABRIC AND BLIND FABRIC FLOW

## Purchase Flow

1. **Purchase Order**: 
   - Create manually or Purchase Order From File (if needed) 
   - *Delivery To*: My Company: Receipts (Fabric) 

*. Purchase order From File
   - Excel file should include the following columns: `Product`, `Quantity`, `Price`, `Lot/Packages`.
   - If **Price** is not provided, remove the "Lot" column entirely. Do **not** leave it empty—this may cause errors.
     - the system will use the product's default purchase price.
   - If Lot is not provided:
     - 
   
2. **Receipt Step 1** 
   - **Import Picking Lines**: 
     - Use the *Import Picking Lines* feature to create Lots / Serial Numbers. 
     - The Excel file should include the following columns: `Product`, `Quantity`, `Price`, `Lot`. 
     - If **Price** is not provided, the system will use the product's default purchase price. 
     - If **Lot** is not provided: 
       - The system will auto-generate a lot number. 
       - ⚠️ **Important**: If you do not want to provided lots in excel, remove the "Lot" column entirely. Do **not** leave it empty—this may cause errors. 
   - Manually "Validate" the receipt via open receipt picking.
   - Transfer: Vendor → Input 

3. **Receipt Step 2** *(using Barcode > Internal Transfer)* 
   - **Internal Transfer** (Input → Stock/Sub)
   - Scan Lots / Serial Numbers of products currently in the Input location 
   - Scan the Stock/Sub Location barcode (destination) 
   - Validate

## Sale Flow

1. **Sale Order**: 
   - Confirm 
   - Approve Order 

2. **Transfer Details**: 
   - If product is not in Output location 
   - Create automatic transfer from Stock/Sub → Output

3. **Delivery**: 
   - Put in Pack 
   - Validate 
   - Output → Customer 

4. **Cutting to Stock**: 
   - Output → Stock/Sub
   - 1. Scan Lots/Serial Numbers 
   - 2. Scan Stock/Sub Location Barcode 

## Return Flow

1. Open the **Sale Order**, go to the **Delivery** tab. 
2. Click the **Return** button. 

### On Return Screen:
- **Return Location**: Set to **Output** 
  - *(Because product was delivered from Output → Customer; returning means Customer → Output)* 

3. Click **Return** to create a return picking.

### In Return App 
4. Add Lot / Serial Numbers 
5. Validate return picking 

6. Use **Cutting to Stock** to transfer: 
   - From: **Output** 
   - To: **Stock/Sub** 
   - Scan Lots / Serial Numbers of output location.
   - Scan Stock/Sub Location barcode 
   - Validate 
   
---

# TRACK AND BLIND COMPONENT FLOW

## Purchase Flow

1. **Purchase Order**: 
   - Create manually or Purchase Order From File (if needed) 
   - *Delivery To*: My Company: Receipt (Component) 
   
2. **Receipt Step 1** 
   - **Import Picking Lines**: 
     - Use the *Import Picking Lines* feature to create Package. 
     - The Excel file should include the following columns: `Product`, `Quantity`, `packages`
   - Manually "Validate" the receipt via open receipt picking.
   - Transfer: Vendor → Input 

3. **Receipt Step 2** *(using Barcode > Internal Transfer)* 
   - **Internal Transfer** (Input → Stock/Sub)
   - Scan Package name of products currently in the Input location 
   - Scan the Stock/Sub Location barcode (destination) 
   - Validate
   
## Sale Flow

1. **Sale Order**: 
   - Confirm 
   - Approve Order 

2. **Component Internal Transfer**: (Stock/Sub → Component-Output )
   - If product is not in Component-Output location 
   - Scan Package name of products currently in the Stock/sub location.
   - Validate.

3. **Delivery**: 
   - Put in Pack 
   - Validate 
   - Output → Customer 

> ⚠️ Note: **Component products** do not require transfer from Component-Output → Stock/Sub.

## Return Flow

1. Open the **Sale Order**, go to the **Delivery** tab. 
- Click the **Return** button. 

### On Return Screen:
2. **Return Location**: Set to **Output** 
- Click **Return** to create a return picking. 

### In Return App
3. Validate return picking 

4. Use **Inventory Adjuctment** to transfer:
   - From: **Output** 
   - To: **Component-Output** 
   - Add Package Name
   
---

# TRACK AND BLIND FLOW (MAIN PRODUCT)

##TRACK

{Sale Order}-> Confirm

{Track Order} Assing : if Component not in Componet-Output Location -> {Component Internal Transfer} Stock/Sub To Component-Output
{Track Order} Cut Done -> Validate

{Delivery}-> Put In Pack -> Validate
    Component (Component-Output To Virtual Location)
    Main Product (Output To Customers)

{Return}-> Return 
    Main Product (Customer To Output)
    Component (Virtual Location To Component-Output)
    Main Product (Output To Virtual Location)

##BLIND

{Sale Order}-> Confirm

{Fabric Cutting}-> if Order have Blind Fabric

{Track Order} Assing : if Component not in Componet-Output Location -> {Component Internal Transfer} Stock To Component-Output
{Track Order} Cut Done : Validate

{Delivery}-> Put In Pack -> Validate
    Component (Component-Output To Virtual Location)
    Fabric (Output To Virtual Location) if Order have Blind Fabric
    Main Product (Output To Customers)

{Return}-> Return
    Main Product (Customer To Output)
    Component (Virtual Location To Component-Output)
    Main Product (Output To Virtual Location)
    Fabric (Virtual Loaction To Output)

----



Case 1: Inventory Adjustment

    Odoo: Lot-001 = 20 pcs
    Physical: Lot-001 = 25 pcs
    Action: Inventory Adjustment (+5)
    Result: Lot-001 = 25 pcs (stock increased by 5)

Case 2: Lot Adjustment

    Odoo: Lot-001 = 20 pcs, Lot-002 = 0 pcs
    Reality: Lot-001 = 15 pcs, Lot-002 = 5 pcs
    Action: Lot Adjustment (-5 from Lot-001, +5 to Lot-002)
    Result: Lot-001 = 15 pcs, Lot-002 = 5 pcs (total still 20 pcs, only reassigned)
    


