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
- **Manufacture**: Track 
- **Sale**: 
  - Track *(manufactured from Track components)* 
  - Fabric 
  - Track (components sold manually)

---

## Tesro Blind

- **Products**: Blind, Track, Blind Fabric 
- **Purchase**: Blind (components), Track (components), Blind Fabric 
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

- In the **Sales Order**, if the product is available in stock but not in the **Output** location, a **Transfer Detail** needs to be created.
- After the transfer, the **Delivery Order** will show the quantity as available.
- If the Output location does not have stock, the delivery will **not reserve** any quantity.

