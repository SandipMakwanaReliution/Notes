Blind            : Manufacturing <=> Component (Component-Output Location) : Purchase [Packages] => Sales
    Blind Fabric :                             (Output Location)           : Purchase [Lots/Serial Numbers] => Sales

Fabric           :                             (Output Location)           : Purchase [Lots/Serial Numbers] => Sales
Track            : Manufacturing <=> Component (Component-Output Location) : Purchase [Packages] => Sales

Fabric Cutting
1.Select Lot (product location on "Output") > Fabric Ready (state)
2.Cutting Operation > Mark Cutting Done > fabric Done (state)

Blind Order
1.Assign
1.Cut Done > Cutting Done (state)
2.Validate->[Done]

=======================
FABRIC AND BLIND FABRIC
=======================
{Purchase Order}-> Purchase order create manually & file -> Delivery To (My Company: Receipts)
{Import Picking Lines}-> Create Lots/Serailnumber
{Receipt Step 1}-> Vandor To Input (Validate Receipt)
{Receipt Step 2}-> Input To Stock/Sub ("Internal Transfer") -> Scan Lots/Serailnumber -> Scan Stock/Sub Location Barcode 

{Sale Order}-> Confirm -> Approve Order 
{"Transfer Details"}-> Stock/Sub To Output : If Product not in Output Location *Full stock qty [Automatic create a Transfer Details]
{Delivery}-> Put In Pack -> Validate -> Output To Customers -> {Cutting To Stock} Output To Stock/Sub -> Scan Lots/Serailnumber -> Scan Stock/Sub Location Barcode 

{Return}-> Add Lots/Serial number -> Customer To Output (Validate) -> {Cutting To Stock} Output To Stock/Sub -> Scan Lots/Serailnumber -> Scan Stock/Sub Location Barcode 

=========
COMPONENT
=========
{Purchase Order}-> "Purchase" order compulsory create manually, not use file. -> Delivery To (My Company: Receipt Component)
{Import Picking Lines}-> Create Packages 
{Receipt}-> Vandor To Stock (Validate Receipt)

{Sale Order}-> Confirm : Raise Error if not component in Component-Output Location ("Component Internal Transfer" -> Stock To Component-Output) -> Approve
{Delivery}-> Put In Pack -> Validate -> Output To Customers

{Return}-> Return -> Customer To Output (Validate) -> {Inventory Adjuctment}-> Output To Component-Output

TRACK
=====

{Sale Order}-> Confirm
{Track Order} Assing : Raise Error if Component not in Componet-Output Location -> {Component Internal Transfer} Stock To Component-Output
{Track Order} Cut Done -> Validate
{Delivery}-> Put In Pack -> Validate

    Component (Component-Output To Virtual Location)
    Main Product (Output To Customers)

{Return}-> Return 

    Main Product (Customer To Output)
    Component (Virtual Location To Component-Output)
    Main Product (Output To Virtual Location)

BLIND
=====

{Sale Order}-> Confirm
{Fabric Cutting}-> if Order have Blind Fabric
{Track Order} Assing : Raise Error if Component not in Componet-Output Location -> {Component Internal Transfer} Stock To Component-Output
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

=============
FABRIC
=============

Purchase 
=> Vendor To Input
=> Input To Stock\Sub {Internal Transfer}-> Sacn Lot and Location

Sale
=> Stock\Sub To Output {Transfer Details}

Return
=> Output To Stock\Sub {Cutting To Stock}-> Sacn Lot and Location

============
COMPONENT
============

Purchase *Manually
=> Venord To Stock

Sale
=> Stock To Component-Output {Component Internal Transfer}
=> Component-Output To Customer

Return
=> Customer To Output
=> Output To Component-Output {Inventory Adjustment}

============================
SET DELIVERY INFO BY BARCODE
============================
Invoice
.....
.....
Badge ID
space

Salesman/Employee > HR Settings > Badge ID

