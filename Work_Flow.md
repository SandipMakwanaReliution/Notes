# DAZZLE FABRIC

- **Product**: Fabric 
- **Purchase**: Fabric 
- **Manufacture**: No 
- **Sale**: Fabric 

---

# DAZZLE SHOES

- **Companies**: 
  1. DAZZLE SHOES 
  2. LEVIOTTO 

---

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
  - Track (components sold manually)

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

## Korzo

- **Products**: Fabric, Track, Motor 
- **Purchase**: Fabric, Track, Motor 
- **Manufacture**: Fabric 
- **Sale**: 
  - Curtain *(Fabric Cutting, Track, Motor)* 
  - Blackout & Sheer *(Fabric Cutting, Track, Motor)* 
  - Roller *(Fabric)*

---

# APP: Transfer Details

- In the **Sales Order**, if the product is available in stock but not in the **Output** location, a **Transfer Detail** needs to be manage.
- After the transfer, the **Delivery Order** will show the quantity as available.
- If the Output location does not have stock, the delivery will **not reserve** any quantity.

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

# FABRIC AND BLIND FABRIC FLOW

## Purchase Flow

1. **Purchase Order**: 
   - Create manually 
   - Attach file if needed 
   - *Delivery To*: My Company → Receipts 
   
2. **Import Picking Lines**: 
   - Create Lots / Serial Numbers 

3. **Receipt Step 1**: 
   - Vendor → Input 
   - Validate receipt 

4. **Receipt Step 2**: 
   - Input → Stock/Sub (*Internal Transfer*) 
   - Scan Lots/Serial Numbers 
   - Scan Stock/Sub Location Barcode 

---

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
   - Scan Lots/Serial Numbers 
   - Scan Stock/Sub Location Barcode 

---

## Return Flow

1. Add Lot/Serial Number 
2. Customer → Output (Validate) 
3. **Cutting to Stock**: 
   - Output → Stock/Sub 
   - Scan Lots/Serial Numbers 
   - Scan Stock/Sub Location Barcode
