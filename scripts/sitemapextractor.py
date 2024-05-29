from bs4 import BeautifulSoup

sitemap_html = """
<div id="sitemapcontainer-832" class="sitemap">
            <div class="container-fluid">
                <h1 class="sitemap-heading">Sitemap</h1>
                <div class="row row-first">
                    <div class="col-lg-3 col-md-3 col-sm-12">
                        <div class="list-heading-1">
                            <h3>
                                <a title="Book a Test Ride" href="/in/en/forms/book-a-test-ride/" class="custom-btn arrow-r font-subheading sitemapContainerAna">Book a Test Ride</a>
                            </h3>
                        </div>
                    </div>
                
                    <div class="col-lg-3 col-md-3 col-sm-12">
                        <div class="list-heading-1">
                            <h3>
                                <a title="Dealer Locator" href="/in/en/locate-us/dealers/" class="custom-btn arrow-r font-subheading sitemapContainerAna">Dealer Locator</a>
                            </h3>
                        </div>
                    </div>
                
                    <div class="col-lg-3 col-md-3 col-sm-12">
                        <div class="list-heading-1">
                            <h3>
                                <a title="Make It Yours" href="https://makeityours.royalenfield.com/configurator/" class="custom-btn arrow-r font-subheading sitemapContainerAna">Make It Yours</a>
                            </h3>
                        </div>
                    </div>
                </div>
                <div class="row">
                    


    
     
        <div id="SitemapLinkComponent1-5838" class="col-lg-3 col-md-3 col-sm-12">
            <div class="list-heading">
                <h3><a title="Motorcycles" class="headingNameSiteMap">
                       Motorcycles
                    </a>
                    
                </h3>
                <ul class="nav-list">
                    
                    
                        <li class="sitemapLinksAnalytics ">
                            <a title="Shotgun 650" class="linksAnalytics" href="/in/en/motorcycles/shotgun-650/">Shotgun 650</a>
                            
                            
                        </li>
                    
                        <li class="sitemapLinksAnalytics ">
                            <a title="New Himalayan" class="linksAnalytics" href="/in/en/motorcycles/new-himalayan/">New Himalayan</a>
                            
                            
                        </li>
                    
                        <li class="sitemapLinksAnalytics ">
                            <a title="Bullet 350" class="linksAnalytics" href="/in/en/motorcycles/bullet-350/">Bullet 350</a>
                            
                            
                        </li>
                    
                        <li class="sitemapLinksAnalytics ">
                            <a title="Super Meteor 650" class="linksAnalytics" href="/in/en/motorcycles/super-meteor-650/">Super Meteor 650</a>
                            
                            
                        </li>
                    
                        <li class="sitemapLinksAnalytics ">
                            <a title="Hunter 350" class="linksAnalytics" href="/in/en/motorcycles/hunter-350/">Hunter 350</a>
                            
                            
                        </li>
                    
                        <li class="sitemapLinksAnalytics ">
                            <a title="Scram 411" class="linksAnalytics" href="/in/en/motorcycles/scram411/">Scram 411</a>
                            
                            
                        </li>
                    
                        <li class="sitemapLinksAnalytics ">
                            <a title="Classic 350" class="linksAnalytics" href="/in/en/motorcycles/classic-350/">Classic 350</a>
                            
                            
                        </li>
                    
                        <li class="sitemapLinksAnalytics ">
                            <a title="Meteor" class="linksAnalytics" href="/in/en/motorcycles/meteor/">Meteor</a>
                            
                            
                        </li>
                    
                        <li class="sitemapLinksAnalytics ">
                            <a title="Interceptor" class="linksAnalytics" href="/in/en/motorcycles/interceptor/">Interceptor</a>
                            
                            
                        </li>
                    
                        <li class="sitemapLinksAnalytics ">
                            <a title="Continental GT" class="linksAnalytics" href="/in/en/motorcycles/continental-gt/">Continental GT</a>
                            
                            
                        </li>
                    
                </ul>
            </div>
        </div>
    
  

                
                    


    
     
        <div id="SitemapLinkComponent2-8538" class="col-lg-3 col-md-3 col-sm-12">
            <div class="list-heading">
                <h3><a title="Locate Us" class="headingNameSiteMap">
                       Locate Us
                    </a>
                    
                </h3>
                <ul class="nav-list">
                    
                    
                        <li class="sitemapLinksAnalytics ">
                            <a title="Find a Store" class="linksAnalytics" href="/in/en/locate-us/dealers/">Find a Store</a>
                            
                            
                        </li>
                    
                        <li class="sitemapLinksAnalytics ">
                            <a title="Find a Service Center" class="linksAnalytics" href="/in/en/locate-us/service-centres/">Find a Service Center</a>
                            
                            
                        </li>
                    
                        <li class="sitemapLinksAnalytics ">
                            <a title="Genuine Motorcycle Accessories" class="linksAnalytics" href="/in/en/gma/">Genuine Motorcycle Accessories</a>
                            
                            
                        </li>
                    
                        <li class="sitemapLinksAnalytics ">
                            <a title="Garage Cafe" class="linksAnalytics" href="/in/en/locate-us/garagecafe/">Garage Cafe</a>
                            
                            
                        </li>
                    
                        <li class="sitemapLinksAnalytics ">
                            <a title="Vintage Store" class="linksAnalytics" href="/in/en/locate-us/pre-owned/">Vintage Store</a>
                            
                            
                        </li>
                    
                        <li class="sitemapLinksAnalytics ">
                            <a title="Become a Genuine Parts Distributor" class="linksAnalytics" href="/in/en/support/genuine-part-distributor/">Become a Genuine Parts Distributor</a>
                            
                            
                        </li>
                    
                </ul>
            </div>
        </div>
    
  

                
                    


    
     
        <div id="SitemapLinkComponent3-8501" class="col-lg-3 col-md-3 col-sm-12">
            <div class="list-heading">
                <h3><a title="Rides" class="headingNameSiteMap">
                       Rides
                    </a>
                    
                </h3>
                <ul class="nav-list">
                    
                    
                        <li class="sitemapLinksAnalytics ">
                            <a title="Rides" class="linksAnalytics" href="/in/en/rides-calendar/">Rides</a>
                            
                            
                        </li>
                    
                </ul>
            </div>
        </div>
    
  

                
                    


    
     
        <div id="SitemapLinkComponent4-7263" class="col-lg-3 col-md-3 col-sm-12">
            <div class="list-heading">
                <h3><a title="Accessories" class="headingNameSiteMap">
                       Accessories
                    </a>
                    
                </h3>
                <ul class="nav-list">
                    
                    
                        <li class="sitemapLinksAnalytics nav-list-children">
                            <a title="Motorcycles" class="linksAnalytics">Motorcycles</a>
                            
                                <span class="icon-arrow-down sub-links"></span>
                            
                            
                                <ul>
                                    <li>
                                        <a title="Shotgun 650" class="sublinksAnalytics" href="/in/en/gma/shotgun-650/">Shotgun 650</a>
                                    </li>
                                
                                    <li>
                                        <a title="All New Himalayan" class="sublinksAnalytics" href="/in/en/gma/all-new-himalayan/">All New Himalayan</a>
                                    </li>
                                
                                    <li>
                                        <a title="All New Bullet 350" class="sublinksAnalytics" href="/in/en/gma/all-new-bullet-350/">All New Bullet 350</a>
                                    </li>
                                
                                    <li>
                                        <a title="Super Meteor 650" class="sublinksAnalytics" href="/in/en/gma/super-meteor-650/">Super Meteor 650</a>
                                    </li>
                                
                                    <li>
                                        <a title="Hunter 350" class="sublinksAnalytics" href="/in/en/gma/hunter-350/">Hunter 350</a>
                                    </li>
                                
                                    <li>
                                        <a title="Scram 411" class="sublinksAnalytics" href="/in/en/gma/scram411/">Scram 411</a>
                                    </li>
                                
                                    <li>
                                        <a title="All New Classic 350" class="sublinksAnalytics" href="/in/en/gma/classic-350/">All New Classic 350</a>
                                    </li>
                                
                                    <li>
                                        <a title="Meteor 350" class="sublinksAnalytics" href="/in/en/gma/meteor/">Meteor 350</a>
                                    </li>
                                
                                    <li>
                                        <a title="Bullet" class="sublinksAnalytics" href="/in/en/gma/bullet/">Bullet</a>
                                    </li>
                                
                                    <li>
                                        <a title="Himalayan" class="sublinksAnalytics" href="/in/en/gma/himalayan/">Himalayan</a>
                                    </li>
                                
                                    <li>
                                        <a title="Interceptor" class="sublinksAnalytics" href="/in/en/gma/interceptor/">Interceptor</a>
                                    </li>
                                
                                    <li>
                                        <a title="Continental GT" class="sublinksAnalytics" href="/in/en/gma/continental-gt/">Continental GT</a>
                                    </li>
                                
                                    <li>
                                        <a title="Classic UCE" class="sublinksAnalytics" href="/in/en/gma/classic-uce/">Classic UCE</a>
                                    </li>
                                </ul>
                            
                        </li>
                    
                        <li class="sitemapLinksAnalytics nav-list-children">
                            <a title="Category" class="linksAnalytics">Category</a>
                            
                                <span class="icon-arrow-down sub-links"></span>
                            
                            
                                <ul>
                                    <li>
                                        <a title="Protection" class="sublinksAnalytics" href="/in/en/gma/protection/">Protection</a>
                                    </li>
                                
                                    <li>
                                        <a title="Seats" class="sublinksAnalytics" href="/in/en/gma/seats/">Seats</a>
                                    </li>
                                
                                    <li>
                                        <a title="Bodywork" class="sublinksAnalytics" href="/in/en/gma/bodywork/">Bodywork</a>
                                    </li>
                                
                                    <li>
                                        <a title="Luggage" class="sublinksAnalytics" href="/in/en/gma/luggage/">Luggage</a>
                                    </li>
                                
                                    <li>
                                        <a title="Engine" class="sublinksAnalytics" href="/in/en/gma/engine/">Engine</a>
                                    </li>
                                
                                    <li>
                                        <a title="Security and Maintenance" class="sublinksAnalytics" href="/in/en/gma/security-and-maintenance/">Security and Maintenance</a>
                                    </li>
                                
                                    <li>
                                        <a title="Controls" class="sublinksAnalytics" href="/in/en/gma/controls/">Controls</a>
                                    </li>
                                
                                    <li>
                                        <a title="Wheels" class="sublinksAnalytics" href="/in/en/gma/wheels/">Wheels</a>
                                    </li>
                                
                                    <li>
                                        <a title="Electrical" class="sublinksAnalytics" href="/in/en/gma/electrical/">Electrical</a>
                                    </li>
                                </ul>
                            
                        </li>
                    
                        <li class="sitemapLinksAnalytics ">
                            <a title="View Catalogue" class="linksAnalytics" href="https://www.royalenfield.com/flipbook/">View Catalogue</a>
                            
                            
                        </li>
                    
                </ul>
            </div>
        </div>
    
  

                
                    


    
     
        <div id="SitemapLinkComponent5-792" class="col-lg-3 col-md-3 col-sm-12">
            <div class="list-heading">
                <h3><a title="Apparel" class="headingNameSiteMap">
                       Apparel
                    </a>
                    
                </h3>
                <ul class="nav-list">
                    
                    
                        <li class="sitemapLinksAnalytics ">
                            <a title="Gloves" class="linksAnalytics" href="https://store.royalenfield.com/riding-gear/gloves">Gloves</a>
                            
                            
                        </li>
                    
                        <li class="sitemapLinksAnalytics ">
                            <a title="Helmets" class="linksAnalytics" href="https://store.royalenfield.com/riding-gear/helmet">Helmets</a>
                            
                            
                        </li>
                    
                        <li class="sitemapLinksAnalytics ">
                            <a title="Boots" class="linksAnalytics" href="https://store.royalenfield.com/lifestyle-apparel/shoes">Boots</a>
                            
                            
                        </li>
                    
                        <li class="sitemapLinksAnalytics ">
                            <a title="Jackets" class="linksAnalytics" href="https://store.royalenfield.com/riding-gear/riding-jackets">Jackets</a>
                            
                            
                        </li>
                    
                        <li class="sitemapLinksAnalytics ">
                            <a title="MLG 1901" class="linksAnalytics" href="https://store.royalenfield.com/catalogsearch/result/?q=mlg">MLG 1901</a>
                            
                            
                        </li>
                    
                        <li class="sitemapLinksAnalytics ">
                            <a title="T-Shirt" class="linksAnalytics" href="https://store.royalenfield.com/lifestyle-apparel/t-shirt">T-Shirt</a>
                            
                            
                        </li>
                    
                        <li class="sitemapLinksAnalytics ">
                            <a title="Shirts" class="linksAnalytics" href="https://store.royalenfield.com/lifestyle-apparel/shirt">Shirts</a>
                            
                            
                        </li>
                    
                        <li class="sitemapLinksAnalytics ">
                            <a title="Masks" class="linksAnalytics" href="https://store.royalenfield.com/lifestyle-accessories/face-mask">Masks</a>
                            
                            
                        </li>
                    
                        <li class="sitemapLinksAnalytics ">
                            <a title="Bags" class="linksAnalytics" href="https://store.royalenfield.com/lifestyle-accessories/bags">Bags</a>
                            
                            
                        </li>
                    
                        <li class="sitemapLinksAnalytics ">
                            <a title="Belts" class="linksAnalytics" href="https://store.royalenfield.com/lifestyle-accessories/belts">Belts</a>
                            
                            
                        </li>
                    
                        <li class="sitemapLinksAnalytics ">
                            <a title="Headgear" class="linksAnalytics" href="https://store.royalenfield.com/lifestyle-accessories/headgear">Headgear</a>
                            
                            
                        </li>
                    
                        <li class="sitemapLinksAnalytics ">
                            <a title="Wallets" class="linksAnalytics" href="https://store.royalenfield.com/lifestyle-accessories/wallets">Wallets</a>
                            
                            
                        </li>
                    
                </ul>
            </div>
        </div>
    
  

                
                    


    
     
        <div id="SitemapLinkComponent6-2091" class="col-lg-3 col-md-3 col-sm-12">
            <div class="list-heading">
                <h3><a title="Our World" class="headingNameSiteMap" target="_blank" rel="nofollow">
                       Our World
                    </a>
                    
                </h3>
                <ul class="nav-list">
                    
                    
                        <li class="sitemapLinksAnalytics ">
                            <a title="Forum" class="linksAnalytics" href="/in/en/our-world/forum/">Forum</a>
                            
                            
                        </li>
                    
                        <li class="sitemapLinksAnalytics ">
                            <a title="Trip Stories" class="linksAnalytics" href="/in/en/our-world/trip-stories/">Trip Stories</a>
                            
                            
                        </li>
                    
                        <li class="sitemapLinksAnalytics ">
                            <a title="Since 1901" class="linksAnalytics" href="/in/en/our-world/since-1901/">Since 1901</a>
                            
                            
                        </li>
                    
                        <li class="sitemapLinksAnalytics ">
                            <a title="News and Media" class="linksAnalytics" href="/in/en/our-world/media/">News and Media</a>
                            
                            
                        </li>
                    
                        <li class="sitemapLinksAnalytics ">
                            <a title="Careers" class="linksAnalytics" href="https://careers.royalenfield.com/us/en/home">Careers</a>
                            
                            
                        </li>
                    
                        <li class="sitemapLinksAnalytics ">
                            <a title="Wallpapers" class="linksAnalytics" href="/in/en/our-world/wallpaper/">Wallpapers</a>
                            
                            
                        </li>
                    
                        <li class="sitemapLinksAnalytics ">
                            <a title="Custom World" class="linksAnalytics" href="/in/en/customworld/">Custom World</a>
                            
                            
                        </li>
                    
                        <li class="sitemapLinksAnalytics ">
                            <a title="Campaigns" class="linksAnalytics" href="/in/en/our-world/campaigns/">Campaigns</a>
                            
                            
                        </li>
                    
                        <li class="sitemapLinksAnalytics ">
                            <a title="Albums" class="linksAnalytics" href="/in/en/our-world/gallery/photos/">Albums</a>
                            
                            
                        </li>
                    
                        <li class="sitemapLinksAnalytics ">
                            <a title="Brand Videos" class="linksAnalytics" href="/in/en/our-world/gallery/videos/">Brand Videos</a>
                            
                            
                        </li>
                    
                </ul>
            </div>
        </div>
    
  

                
                    


    
     
        <div id="SitemapLinkComponent7-8070" class="col-lg-3 col-md-3 col-sm-12">
            <div class="list-heading">
                <h3><a title="Support" class="headingNameSiteMap">
                       Support
                    </a>
                    
                </h3>
                <ul class="nav-list">
                    
                    
                        <li class="sitemapLinksAnalytics ">
                            <a title="Contact Us" class="linksAnalytics" href="/in/en/support/contact-us/">Contact Us</a>
                            
                            
                        </li>
                    
                        <li class="sitemapLinksAnalytics ">
                            <a title="Write to Us" class="linksAnalytics" href="/in/en/support/">Write to Us</a>
                            
                            
                        </li>
                    
                        <li class="sitemapLinksAnalytics ">
                            <a title="FAQ's" class="linksAnalytics" href="https://www.royalenfield.com/in/en/support/#faq">FAQ's</a>
                            
                            
                        </li>
                    
                        <li class="sitemapLinksAnalytics ">
                            <a title="Road Side Assistance" class="linksAnalytics" href="/in/en/support/road-side-assistance/">Road Side Assistance</a>
                            
                            
                        </li>
                    
                        <li class="sitemapLinksAnalytics ">
                            <a title="Owner's Manual" class="linksAnalytics" href="/in/en/support/owners-manual/">Owner's Manual</a>
                            
                            
                        </li>
                    
                        <li class="sitemapLinksAnalytics ">
                            <a title="Quick Start Guide" class="linksAnalytics" href="/in/en/support/digital-quickstart/">Quick Start Guide</a>
                            
                            
                        </li>
                    
                        <li class="sitemapLinksAnalytics ">
                            <a title="Private Import Policy" class="linksAnalytics" href="/in/en/legal/private-import-policy/">Private Import Policy</a>
                            
                            
                        </li>
                    
                        <li class="sitemapLinksAnalytics ">
                            <a title="Privacy" class="linksAnalytics" href="/in/en/legal/privacy-policy/">Privacy</a>
                            
                            
                        </li>
                    
                        <li class="sitemapLinksAnalytics ">
                            <a title="Terms &amp; Conditions" class="linksAnalytics" href="/in/en/legal/terms-and-conditions/">Terms &amp; Conditions</a>
                            
                            
                        </li>
                    
                        <li class="sitemapLinksAnalytics ">
                            <a title="Cookies" class="linksAnalytics" href="/in/en/legal/cookie-policy/">Cookies</a>
                            
                            
                        </li>
                    
                </ul>
            </div>
        </div>
    
  

                
                    


    
     
        <div id="SitemapLinkComponent8-9327" class="col-lg-3 col-md-3 col-sm-12">
            <div class="list-heading">
                <h3><a title="Finance" class="headingNameSiteMap">
                       Finance
                    </a>
                    
                </h3>
                <ul class="nav-list">
                    
                    
                        <li class="sitemapLinksAnalytics ">
                            <a title="Finance English" class="linksAnalytics" href="/in/en/finance/">Finance English</a>
                            
                            
                        </li>
                    
                        <li class="sitemapLinksAnalytics ">
                            <a title="Finance Hindi" class="linksAnalytics" href="/in/hi/finance/">Finance Hindi</a>
                            
                            
                        </li>
                    
                </ul>
            </div>
        </div>
    
  

                
                    


                </div>
            </div>
        </div>
"""

soup = BeautifulSoup(sitemap_html, 'html.parser')

# Find all <a> tags within the sitemap container
sitemap_links = soup.select('.sitemap a[href]')

# Extract URLs from the href attribute of each <a> tag
urls = [link['href'] for link in sitemap_links]

print(urls)