// build console output
function buildOutput(securityHint)
{
    const lenToken = securityHint.length;
    var headerContent = "GET LOGO! Security-Hint";
    var strLine       = "+";
    var strToken      = "| " + securityHint;
    var strHeader     = "| " + headerContent;
    var strPadding    = "|";

    for (let index = 0; index < lenToken + 2; index++) {
        strLine = strLine + "-";
        strPadding = strPadding + " ";

        if ( index > headerContent.length )
        {
            strHeader = strHeader + " ";
        }

    }

    strLine    = strLine + "+";
    strHeader  = strHeader + "|";
    strPadding = strPadding + "|";
    strToken   = strToken + " |";

    console.debug(
        strLine + "\n" +
        strHeader + "\n" +
        strLine + "\n" +
        strPadding + "\n" +
        strToken + "\n" +
        strPadding + "\n" +
        strLine + "\n"
    )
}

// get current security hint
function getSecurityHint(output = false)
{
    let url = window.location.href; 
    temp = new URLSearchParams(url);

    let securityHint = temp.get('Security-Hint') != null
        ? temp.get('Security-Hint')
        : false;

    if ( output )
    {
        buildOutput(securityHint)
    }

    return securityHint
}

// write security hint into local file
const downloadToFile = (content, filename, contentType) => {
    const a = document.createElement('a');
    const file = new Blob([content], {type: contentType});
    
    a.href= URL.createObjectURL(file);
    a.download = filename;
    a.click();
  
      URL.revokeObjectURL(a.href);
  };

if ( getSecurityHint() )
{
    downloadToFile(getSecurityHint(true), 'security_hint.txt', 'text/plain');
}

