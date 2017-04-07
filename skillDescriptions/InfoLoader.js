function loader (){
    var str = String(location.pathname.split("/").slice(-1));
    var str2 = str.replace('.html','');
    var fileName = str2.replace(/%20/g,' ');
    var imagestr = str2+".jpg";
    var image = imagestr.toLowerCase();
    document.write("<h2>"+fileName+"</h2>");
    document.write("<img src="+image+" alt='Skill neighborhood image'>");
}
loader()