function goToUrl(url) {
    window.location = getBaseUrl() + url;
}

function getBaseUrl() {
    // TODO Cambiar si local
    var getUrl = window.location;
    var baseUrl = getUrl.protocol + "//" + getUrl.host + "/" + getUrl.pathname.split('/')[0];
    return baseUrl;
}