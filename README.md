# ship_dimensions
Software to search ships close to a certain characteristics (i.e. deadweight, length, width and draught) and to generate a technical drawing in .dxf format.
The software tool is available at:
https://portdesigntoolkit.pro/ships/dimensions/

## Introduction
One of the key parameters determining a seaport's throughput capacity is the design capacity of the vessel. Design capacity refers to a vessel with the maximum dimensions the port can accommodate. The characteristics of the design capacity of the vessel determine the potential throughput of the port, as well as the capital and operating costs required to create and maintain the port infrastructure, including berths, access channels, and waters.
In seaport design practice, there are two approaches to selecting a design vessel: direct and inverse. These approaches can be compared to greenfield and brownfield projects []. In the direct approach, the design vessel must be selected based on current market conditions, the port's potential cargo turnover, and its competitive strategy. From this perspective, selecting a design vessel is a marketing analysis question that asks, "What can I know? What can I hope for? What should I do?". In this approach, the design vessel is used to determine the dimensions of approach channels, water areas, and berth depths.
In the reverse formulation of the problem, the design vessel is determined based on the characteristics of an existing seaport. In this case, the question arises: which vessels operating in a given region can be handled at a given port? This question is often raised during the reorganization or reconstruction of an existing terminal when new cargo flows emerge. This problem becomes especially relevant during periods of change, when cargo flows are rerouted from one port to another. A striking example is the rerouting of cargo flows during the 2019-2020 pandemic, when large container terminals were so overloaded that shipping companies were forced to reroute cargo flows to neighboring feeder ports.
The described task is key in seaport design, as its outcome determines all port design parameters. Therefore, methods for justifying design vessels receive special attention in seaport design theory. This article provides an overview of existing methods for justifying design vessel selection, as well as a description of a software tool for analyzing and developing justifications based on these methods.
## Methods and materials
The main methods for selecting a design vessel are:
    economic;
    reference;
    statistical;
    marketing analysis.
The economic method is based on calculating the cost of transporting a specific type of cargo. This method collects data on transportation distances, the characteristics and costs of various vessels, port handling times, crew numbers and wages, fuel consumption and costs, current and projected freight rates, and port and canal dues. After collecting the data, the cost of transportation is calculated, and the optimal vessel is selected. The optimal vessel, according to this method, is the one that provides the greatest difference between the freight rate and the cost price . This method is widely used by companies that own their own fleets and have access to accurate information on vessel characteristics. Recently, it has rarely been used by design organizations due to a lack of sufficient information.
In the absence of information, design organizations are increasingly using reference methods. A number of domestic and international organizations periodically publish reference books containing information on the characteristics and distribution of vessels of various classes. The most well-known Russian reference books are the CNIIMF reports, while the most well-known international reference books are the PIANC reports []. PIANC reports are increasingly preferred in design practice , as they provide not only reference data but also theoretical materials on vessel characteristics and a description of the data collection and analysis methods. The main drawback of reference data is the infrequent updating and categorization of data: the reports only provide information for a specific category of vessels.
Each reference book is developed based on an analysis of statistical data on the composition of the maritime fleet. Conducting such an analysis during port design allows for significantly more information about the existing fleet. However, the large volume of information makes it difficult to form a clear understanding of the fleet being analyzed. Therefore, the analysis typically involves creating a correlation-regression model that structures the relationship between a vessel's deadweight and its key dimensions, including length, width, and draft []. An example of the regression is shown in Figure 1 .

<img src="https://github.com/aseemyonov054/ship_dimensions/blob/main/imgs/img1.png"/>
Figure 1. The dependence of the vessel length on the deadweight, determined by the method of correlation-regression analysis.

Regressions allow us to estimate the key characteristics of vessels of a given deadweight and obtain information about which existing vessels can be considered as design vessels. This method can be used both to improve the search for large amounts of information and for a preliminary assessment of the characteristics of a design vessel.
Marketing analysis involves collecting data on the existing fleet, fleet development trends, vessel order volumes in various regions of the world, and the fleet handled in neighboring ports. Based on this data, a forecast is made of the characteristics of potential vessels that can be handled in the planned port. This analysis is performed in the early stages of a project, forming the initial data for subsequent stages . In domestic practice, such tasks are typically performed by consulting rather than design firms, as the analysis requires extensive data collection and time-consuming statistical analysis. In some cases, marketing analysis may include the use of economic, reference, and statistical methods.
Each method has its own level of result reliability. Regardless of the chosen substantiation method, the task of selecting a design vessel is labor-intensive and challenging. Therefore, software tools that reduce the labor-intensive nature of information searches are becoming increasingly important. The following section describes one such tool.
## Results
The software tool is designed to search for vessel characteristics using several sources and methods:
    according to the PIANC reference book;
    by the method of correlation-regression analysis;
    according to open court databases.
To search for information, select on the main screen:
    vessel type – the presented version of the software tool includes tankers, bulk carriers, container ships and gas carriers;
    the characteristic by which the search will be performed – deadweight, length, width or draft of the vessel;
    the value by which the search will be performed - for example, deadweight 50,000 tons. The software tool provides a field that suggests the boundaries within which the search can be performed;
    Search accuracy – a percentage value that determines how close the values should be to each other. For example , 50,000 deadweight – ±10 %.
The main screen of the software tool is shown in Fig. 2 .
 
Figure 2. The main screen of the ship search software tool

The search results are:
    - data from the PIANC directory (Fig. 3 ).
 
Figure 3. Example of search results: data from the PIANC directory

    - data on the assessment of vessel characteristics using the correlation-regression analysis method (Fig. 4 ).
 
Figure 4. Example of search results: correlation-regression analysis data

The data is supported by regression graphs for the vessel's length, width, and draft. Clicking on the graph title in the legend hides the corresponding regression graph (Figure 5 ).
     
a) graphs of three regressions	b) graphs of two regressions
Figure 5. Example of search results: regression graphs of the length, width, and draft of a vessel on deadweight

    -data on courts from public sources (Fig . 6 ).
 
Figure 6: Example of search results: data from public sources

The list of vessels is sorted by absolute proximity to the desired parameter value. Clicking on a vessel's IMO code takes you to one of the public sources providing information on the vessel's flag, position, and media data (Fig. 7 ).
 
Figure 7. Example of information from public sources

The general appearance of the search result interface is shown in Fig. 8 .
 
Figure 8. Search results interface

Each data group is accompanied by a "Download Drawing" button, which calls a function that generates a dimensional drawing of the vessel with the corresponding dimensions in DXF format . DXF (from the English " Drawing" The DWG (Drawing Format) is an open file format for exchanging graphical information between computer-aided design (CAD) applications. The format was created by Autodesk for the AutoCAD system. Currently , Autodesk prefers to use the proprietary DWG ( Drawing ) format . However, most competing CAD systems, including open-source CAD systems, prefer to work with the DXF format. Figure 9 shows an example of a generated drawing.
 
Figure 9. Example of a generated drawing
The development of the software tool involves the addition of functions for calculating parameters and generating drawings of the seaport water area, as well as using information to determine the parameters of technological equipment for the sea cargo front.


