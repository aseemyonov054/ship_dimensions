# ship_dimensions
Software to search ships close to a certain characteristics (i.e. deadweight, length, width and draught) and to generate a technical drawing in .dxf format.
The software tool is available at:
https://portdesigntoolkit.pro/ships/dimensions/

## Introduction
One of the key parameters determining a seaport's throughput capacity is the design vessel. Design vessel refers to a ship with the maximum dimensions that port can accommodate. The characteristics of the design vessel determine the potential throughput of the port, as well as the capital and operating costs required to create and maintain the port infrastructure, including berths, approach channels and operational water areas.
In seaport design practice, there are two approaches to selecting a design vessel: direct and reverse. These approaches can be compared to greenfield and brownfield projects [1-2]. In the direct approach, the design vessel must be selected based on current market conditions, the port's potential cargo turnover, and its competitive strategy. From this perspective, selecting a design vessel is a marketing analysis question that asks, "What can I know? What can I hope for? What should I do?" [3]. In this approach, the design vessel is used to determine the dimensions of approach channels, operational water areas, and berth depths.
In the reverse formulation of the problem, the design vessel is determined based on the characteristics of an existing seaport. In this case, the question arises: which vessels operating in a given region can be handled at a given port? This question is often raised during the reorganization or reconstruction of an existing terminal when new cargoflows emerge. This problem becomes especially relevant during periods of change, when cargo flows are rerouted from one port to another. A striking example is the rerouting of cargo flows during the 2019-2020 pandemic, when large container terminals were so overloaded that shipping companies were forced to reroute cargo flows to neighboring feeder ports [4-5].
The described task is key in seaport design, as its outcome determines all port design parameters. Therefore, methods for justifying design vessels receive special attention in seaport design theory. This article provides an overview of existing methods for justifying design vessel selection, as well as a description of a software tool for analyzing and developing justifications based on these methods.

## Methods of design ship' selection
The main methods for selecting a design vessel are:
	1) economic;
	2) reference book;
	3) statistical;
	4) marketing.
The economic method is based on calculating the cost of transporting a specific type of cargo [6]. This method collects data on transportation distances, the characteristics and costs of various vessels, port cargo handling time, crew number and wage, fuel consumption and cost, current and projected freight rates, port and canal dues. After collecting the data, the cost of transportation is calculated, and the optimal vessel is selected. The optimal vessel, according to this method, is the one that provides the greatest difference between the freight rate and the shipping cost This method is widely used by companies that possess their own fleets and have access to accurate information on vessel characteristics. Recently, it has rarely been used by design organizations due to a lack of sufficient information.
In the absence of information, design organizations are increasingly using reference methods. A number of domestic and international organizations periodically publish reference books containing information on the characteristics and distribution of vessels of various classes. The most known are the PIANC reports, which are increasingly preferred in design practice, as they provide not only reference data but also theoretical materials on vessel characteristics and a description of the data collection and analysis methods [7]. The main drawback of reference data is the infrequent updating and categorization of data: the reports only provide information for a specific category of vessels.
Each reference book is developed based on an analysis of statistical data on the composition of the maritime fleet. Conducting such an analysis during port design allows for significantly more information about the existing fleet. However, the large volume of information makes it difficult to form a clear understanding of the fleet being analyzed. Therefore, the analysis typically involves creating a regression model that structures the relationship between a vessel's deadweight and its key dimensions, including length, width, and draft [8]. An example of the regression is shown in Fig.1.

<img src="https://github.com/aseemyonov054/ship_dimensions/blob/main/imgs/img1.png"/>

Figure 1. The dependence of the vessel length on the deadweight, determined by the method of correlation-regression analysis.

Regressions allow us to estimate the key characteristics of vessels of a given deadweight and obtain information about which existing vessels can be considered as design vessels. This method can be used both to improve the search for large amounts of information and for a preliminary assessment of the characteristics of a design vessel.
Marketing involves collecting data on the existing fleet, fleet development trends, vessel order volumes in various regions of the world, and the fleet handled in neighboring ports. Based on this data, a forecast is made of the characteristics of potential vessels that can be handled in the planned port. This analysis is performed in the early stages of a project, forming the initial data for subsequent stages. In domestic practice, such tasks are typically performed by consulting companies, as the analysis requires extensive data collection and time-consuming statistical analysis. In some cases, marketing analysis may include the use of economic, reference, and statistical methods.
Each method has its own level of result reliability. Regardless of the chosen substantiation method, the task of selecting a design vessel is labor-intensive and challenging. Therefore, software tools that reduce the labor-intensive nature of information searches are becoming increasingly important. The following section describes one such tool.

## Tool description
The software tool is designed to search for vessel characteristics using several sources and methods:
	1) according to the PIANC reference book;
	2) by the method of correlation-regression analysis;
	3) according to open court databases [9].
To search for information, select on the main screen:
	1) vessel type – the presented version of the software tool includes tankers, bulk carriers, container ships and gas carriers;
	2) the characteristic by which the search will be performed – deadweight, length, width or draft of the vessel;
	3) the value by which the search will be performed - for example, deadweight 50,000 tons. The software tool provides a field that suggests the boundaries within which the search can be performed;
	4) search accuracy – a percentage value that determines how close the values should be to each other. For example , 50,000 deadweight – ±10 %.
The main screen of the software tool is shown in Fig. 2 .

<img src="https://github.com/aseemyonov054/ship_dimensions/blob/main/imgs/img2.png"/>
Figure 2. The main screen of the ship search software tool

The search results are:
	1) data from the PIANC directory (Fig. 3).

<img src="https://github.com/aseemyonov054/ship_dimensions/blob/main/imgs/img3.png"/>
Figure 3. Example of search results: data from the PIANC directory

    2) data on the assessment of vessel characteristics using the correlation-regression analysis method (Fig. 4).

 
<img src="https://github.com/aseemyonov054/ship_dimensions/blob/main/imgs/img4.png"/>
Figure 4. Example of search results: correlation-regression analysis data

The data is supported by regression graphs for the vessel's length, width, and draft. Clicking on the graph title in the legend hides the corresponding regression graph (Fig. 5).

<img src="https://github.com/aseemyonov054/ship_dimensions/blob/main/imgs/img5-1.png"/>
Figure 5. Example of search results: regression graphs of the length, width, and draft of a vessel on deadweight

	3) data on courts from public sources (Fig. 6).
 
<img src="https://github.com/aseemyonov054/ship_dimensions/blob/main/imgs/img6.png"/>
Figure 6: Example of search results: data from public sources

The list of vessels is sorted by absolute proximity to the desired parameter value. Clicking on a vessel's IMO code takes you to one of the public sources providing information on the vessel's flag, position, and media data (Fig. 7).
 
<img src="https://github.com/aseemyonov054/ship_dimensions/blob/main/imgs/img7.png"/>
Figure 7. Example of information from public sources

The general appearance of the search result interface is shown in Fig. 8.
 
<img src="https://github.com/aseemyonov054/ship_dimensions/blob/main/imgs/img8.png"/>
Figure 8. Search results interface

Each data group is accompanied by a "Download Drawing" button, which calls a function that generates a dimensional drawing of the vessel with the corresponding dimensions in DXF format . DXF is an open file format for exchanging graphical information between computer-aided design (CAD) applications. The format was created by Autodesk for the AutoCAD system [Wiki]. Currently, Autodesk prefers to use the proprietary DWG (drawing) format . However, most competing CAD systems, including open-source CAD systems, prefer to work with the DXF format [wiki]. Fig. 9 shows an example of a generated drawing.


<img src="https://github.com/aseemyonov054/ship_dimensions/blob/main/imgs/img9.png"/>
Figure 9. Example of a generated drawing

The development of the software tool involves the addition of functions for calculating parameters and generating drawings of the seaport water area, as well as using information to determine the parameters of technological equipment for the sea cargo front.

## References
1) PIANC – Greenfield
2) PIANC – Brownfield
3) Critique of Pure Reason
4) UNCTAD – COVID 2019
5) COVID19 news
6) Maritime economics
7) PIANC – ships’ dimensions
8) Regression
9) Vessel Finder
10) Wiki – DXF
11) Wiki - CAD



