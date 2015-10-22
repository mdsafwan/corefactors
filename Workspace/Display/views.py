from django.http import HttpResponse, Http404
from django.template import Context, Template
from django.template.loader import get_template, render_to_string
#from stripogram import html2text
from django.shortcuts import render
from Display.models import landingPageData, landingPageMaster
import json

def recievedata(request):
    content1 = request.POST.get('content1')
    content2 = request.POST.get('content2')
    content2 = json.loads(content2)
    for html_data in content2:
        print html_data
        print "editor : " ,html_data[0]
        print "html : ",html_data[1]
    #for i in range(0,int(content1)):
     #   print content2[i]
#         print content2[i][1]
#         

    #tpl = request.POST.get('tpl')
    #return HttpResponse("Hello")

#     companyname = request.POST.get('content1')
#     tagline = request.POST.get('content2')
#     coverphotoinfo = request.POST.get('content3')
#     servicesheading = request.POST.get('content4')
#     servicesinfo = request.POST.get('content5')     
#     service1img = request.POST.get('content6')      
#     service1info = request.POST.get('content7')   
#     service2info = request.POST.get('content8')
#     service2img = request.POST.get('content9')
#     galleryheading = request.POST.get('content10')
#     galleryimg1 = request.POST.get('content11')
#     galleryimg2 = request.POST.get('content12')
#     galleryimg3 = request.POST.get('content13')
#     galleryimg4 = request.POST.get('content14')
#     galleryimg5 = request.POST.get('content15')
#     galleryimg6 = request.POST.get('content16')
#     feature1heading = request.POST.get('content17')
#     feature1info = request.POST.get('content18')
#     feature2heading = request.POST.get('content19')
#     feature2info = request.POST.get('content20')
#     feature3heading = request.POST.get('content21')
#     feature3info = request.POST.get('content22')
#     aboutusinfo = request.POST.get('content23')
#     getinformedheading = request.POST.get('content24')
#     getinformedinfo = request.POST.get('content25')
#     copyrightinfo = request.POST.get('content26')
#     coverphotoimg = request.POST.get('content27')
# 
# 
#     masterdata= landingPageMaster.objects.create(templatename='Template1')
#     landingPageData.objects.create(m_landingpage = masterdata, 
#                                    companyname_html = companyname, 
#                                    tagline_html = tagline,
#                                    coverphotoinfo_html = coverphotoinfo,
#                                    servicesheading_html = servicesheading,
#                                    servicesinfo_html = servicesinfo,
#                                    service1img_html = service1img,
#                                    service1info_html = service1info,
#                                    service2info_html = service2info,
#                                    service2img_html = service2img,
#                                    galleryheading_html = galleryheading,
#                                    galleryimg1_html = galleryimg1,
#                                    galleryimg2_html = galleryimg2,
#                                    galleryimg3_html = galleryimg3,
#                                    galleryimg4_html = galleryimg4,
#                                    galleryimg5_html = galleryimg5,
#                                    galleryimg6_html = galleryimg6,
#                                    feature1heading_html = feature1heading, 
#                                    feature1info_html = feature1info,
#                                    feature2heading_html = feature2heading,
#                                    feature2info_html = feature2info,
#                                    feature3heading_html = feature3heading,
#                                    feature3info_html = feature3info,
#                                    aboutusinfo_html = aboutusinfo,
#                                    getinformedheading_html = getinformedheading,
#                                    getinformedinfo_html = getinformedinfo,
#                                    copyrightinfo_html = copyrightinfo,
#                                    coverphotoimg_html = coverphotoimg
#                                    )
    
    
def displaypage(request):
    return render(request, "landingpageeditor.html", {})

def generatelandingpage(request):
    if request.GET.get('lp'):
        lp_id = request.GET.get('lp')
        masterdata= landingPageMaster.objects.filter(uniqueid=lp_id).last()
        landing_data = landingPageData.objects.filter(m_landingpage_id=masterdata.id).last()
        companyname = landing_data.companyname_html
        tagline = landing_data.tagline_html
        coverphotoinfo = landing_data.coverphotoinfo_html
        servicesheading = landing_data.servicesheading_html
        servicesinfo = landing_data.servicesinfo_html
        service1img = landing_data.service1img_html
        service1info = landing_data.service1info_html
        service2info = landing_data.service2info_html
        service2img = landing_data.service2img_html
        galleryheading = landing_data.galleryheading_html
        galleryimg1 = landing_data.galleryimg1_html
        galleryimg2 = landing_data.galleryimg2_html
        galleryimg3 = landing_data.galleryimg3_html
        galleryimg4 = landing_data.galleryimg4_html
        galleryimg5 = landing_data.galleryimg5_html
        galleryimg6 = landing_data.galleryimg6_html
        feature1heading = landing_data.feature1heading_html
        feature1info = landing_data.feature1info_html
        feature2heading = landing_data.feature2heading_html
        feature2info = landing_data.feature2info_html
        feature3heading = landing_data.feature3heading_html
        feature3info = landing_data.feature3info_html
        aboutusinfo = landing_data.aboutusinfo_html
        getinformedheading = landing_data.getinformedheading_html
        getinformedinfo = landing_data.getinformedinfo_html
        copyrightinfo = landing_data.copyrightinfo_html
        coverphotoimg = landing_data.coverphotoimg_html
            

#     companyname = request.POST.get('content1')
#     tagline = request.POST.get('content2')
#     coverphotoinfo = request.POST.get('content3')
#     #coverphotoinfo = html2text(coverphotoinfo)
#     servicesheading = request.POST.get('content4')
#     servicesinfo = request.POST.get('content5')
#     service1img = request.POST.get('content6')  
#     service1info = request.POST.get('content7')
#     service2info = request.POST.get('content8')
#     service2img = request.POST.get('content9')
#     galleryheading = request.POST.get('content10')
#     galleryimg1 = request.POST.get('content11')
#     galleryimg2 = request.POST.get('content12')
#     galleryimg3 = request.POST.get('content13')
#     galleryimg4 = request.POST.get('content14')
#     galleryimg5 = request.POST.get('content15')
#     galleryimg6 = request.POST.get('content16')
#     feature1heading = request.POST.get('content17')
#     feature1info = request.POST.get('content18')
#     feature2heading = request.POST.get('content19')
#     feature2info = request.POST.get('content20')
#     feature3heading = request.POST.get('content21')
#     feature3info = request.POST.get('content22')
#     aboutusinfo = request.POST.get('content23')
#     getinformedheading = request.POST.get('content24')
#     getinformedinfo = request.POST.get('content25')
#     copyrightinfo = request.POST.get('content26')
#     coverphotoimg = request.POST.get('content27')


    template = get_template('landingpagetemplate.html')
    html = template.render(Context({"CompanyNameTag" : companyname,
                                    "TaglineTag" : tagline,
                                    "CoverPhotoInfoTag" : coverphotoinfo,
                                    "ServicesHeadingTag" : servicesheading,
                                    "ServicesInfoTag" : servicesinfo,
                                    "Service1ImgTag" : service1img,
                                    "Service1InfoTag" : service1info,
                                    "Service2InfoTag" : service2info,
                                    "Service2ImgTag" : service2img,
                                    "GalleryHeadingTag" : galleryheading,
                                    "GalleryImg1Tag" : galleryimg1,
                                    "GalleryImg2Tag" : galleryimg2,
                                    "GalleryImg3Tag" : galleryimg3,
                                    "GalleryImg4Tag" : galleryimg4,
                                    "GalleryImg5Tag" : galleryimg5,
                                    "GalleryImg6Tag" : galleryimg6,
                                    "Feature1HeadingTag" : feature1heading,
                                    "Feature1InfoTag" : feature1info,
                                    "Feature2HeadingTag" : feature2heading,
                                    "Feature2InfoTag" : feature2info,
                                    "Feature3HeadingTag" : feature3heading,
                                    "Feature3InfoTag" : feature3info,
                                    "AboutUsInfoTag" : aboutusinfo,
                                    "GetInformedHeadingTag" : getinformedheading,
                                    "GetInformedInfoTag" : getinformedinfo,
                                    "CopyrightInfoTag" : copyrightinfo,
                                    "CoverPhotoImgTag" : coverphotoimg,
                                    }))
    return HttpResponse(html)

