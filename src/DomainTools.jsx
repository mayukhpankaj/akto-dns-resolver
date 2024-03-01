import React, { useState, useRef, useEffect } from "react"
// import { addClass, useExternalScripts } from "./UseExternalScripts.js"
// import { addPropertyControls, ControlType } from "framer"
import clipboardCopy from "clipboard-copy"
import DNScodes from "./DNScodes"
import { v4 as uuidv4 } from 'uuid';




export default function DomainTools(props) {

    // useExternalScripts(
    //     "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"
    // )

    // useExternalScripts(
    //     "https://d1hvi6xs55woen.cloudfront.net/website-assets/polaris.css"
    // )

    const [inputValue, setinputValue] = useState("")
    const [outputValue, setoutputValue] = useState("")
    const [isError, setError] = useState(false)
    const [isClicked, setIsClicked] = useState(false)
    const [errMessage,setErrorMessage] = useState('')
    const [selectedOption, setSelectedOption] = useState('ALL');
    const [selectedLabel, setSelectedLabel] = useState('ALL');


  const handleOptionChange = (e) => {
    setSelectedOption(e.target.value);
    console.log(e.target.value)


  };


    const DNSerrors = {
        "0": {"code": 0, "name": "NoError", "meaning": "No Error"},
        "1": {"code": 1, "name": "FormErr", "meaning": "Format Error"},
        "2": {"code": 2, "name": "ServFail", "meaning": "Server Failure"},
        "3": {"code": 3, "name": "NXDomain", "meaning": "Non-Existent Domain"},
        "4": {"code": 4, "name": "NotImp", "meaning": "Not Implemented"},
        "5": {"code": 5, "name": "Refused", "meaning": "Query Refused"},
        "6": {"code": 6, "name": "YXDomain", "meaning": "Name Exists when it should not"},
        "7": {"code": 7, "name": "YXRRSet", "meaning": "RR Set Exists when it should not"},
        "8": {"code": 8, "name": "NXRRSet", "meaning": "RR Set that should exist does not"},
        "9": {"code": 9, "name": "NotAuth", "meaning": "Server Not Authoritative for zone"},
        "10": {"code": 10, "name": "NotAuth", "meaning": "Not Authorized"},
        "11": {"code": 11, "name": "DSOTYPENI", "meaning": "DSO-TYPE Not Implemented"},
        "16": {"code": 16, "name": "BADVERS", "meaning": "Bad OPT Version"},
        "16": {"code": 16, "name": "BADSIG", "meaning": "TSIG Signature Failure"},
        "17": {"code": 17, "name": "BADKEY", "meaning": "Key not recognized"},
        "18": {"code": 18, "name": "BADTIME", "meaning": "Signature out of time window"},
        "19": {"code": 19, "name": "BADMODE", "meaning": "Bad TKEY Mode"},
        "20": {"code": 20, "name": "BADNAME", "meaning": "Duplicate key name"},
        "21": {"code": 21, "name": "BADALG", "meaning": "Algorithm not supported"},
        "22": {"code": 22, "name": "BADTRUNC", "meaning": "Bad Truncation"},
        "23": {"code": 23, "name": "BADCOOKIE", "meaning": "Bad/missing Server Cookie"}
      }
      



    const domainRegex = /(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z0-9][a-z0-9-]{0,61}[a-z0-9]/g;

    // useEffect(() => {
    //     // Update output whenever inputvalue changes
    //     if (inputValue === "") {
    //         setError(false)
    //         setoutputValue("")
    //     } else {
    //             // checking the domain as user enter the input.. not looks so user friendly .
    //                     // if (domainRegex.test(inputValue)) {
    //                     //     // Valid domain, you can proceed with DNS lookup or other actions
    //                     //     setError(false)
    //                     //     console.log('Valid domain:', inputValue);
    //                     //     // Perform DNS lookup or other actions here
    //                     //   } else {
    //                     //     // Invalid domain, show error message
    //                     //     setError(true)
    //                     //     setErrorMessage('Invalid domain name');     
    //                     //     console.log('Invalid domain:', inputValue);
    //                     //   }
    //     }
    // }, [inputValue])


    async function fetchDNSData(domain, recordType) {
        let rr_type = selectedOption
        const apiUrl = `https://dns.google/resolve?name=${domain}&type=${rr_type}`;
        // const apiUrl = `https://dns.google/resolve?name=${domain}&type=${recordType}`;

        console.log(apiUrl)
      
        try {
          const response = await fetch(apiUrl, {
            headers: {
              'accept': 'application/dns-json'
            }
          });
      
          if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
          }
      
          const data = await response.json();
        
          return data;
        } catch (error) {
          console.error('Error fetching DNS data:', error.message);
          throw error; // Rethrow the error to handle it in the calling code if needed
        }
      }
      
      


    const handleDNS = ()=>{
        
        console.log(inputValue)
        console.log("button clicked")

        console.log(selectedOption)




    const domainRegex = /(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z0-9][a-z0-9-]{0,61}[a-z0-9]/g;

    if (domainRegex.test(inputValue)) {
      // Valid domain, you can proceed with DNS lookup or other actions
      setErrorMessage('');
      setError(false)
      console.log('Valid domain:', inputValue);

      setoutputValue('Sending packets, please wait...')

      setIsClicked(true)

      fetchDNSData(inputValue, 'ALL')
      .then((result) => {
        console.log('DNS API response:', result);
        // Handle the DNS JSON data here
        console.log(result['Answer'])

        if(result['Status'] ===0){

                let outputscreen =''
                
                if(result['Answer']){
                    result['Answer'].forEach(obj => {

                        if(DNScodes.hasOwnProperty(obj.type)){
                           var codec =  DNScodes[(obj.type)].type;
                        }
                        
    
                        outputscreen += `${codec} : ${obj.data} \n`;
                    });
    
                }
                else if(result['Authority']){

                    result['Authority'].forEach(obj => {

                        if(DNScodes.hasOwnProperty(obj.type)){
                           var codec =  DNScodes[(obj.type)].type;
                        }
                        
    
                        outputscreen += `${codec} : ${obj.data} \n`;
                    });



                }



                console.log(outputscreen)
                setoutputValue(outputscreen)
          
        }
        else{
                setError(true)
                setErrorMessage('This domain does not exist')
                setoutputValue(DNSerrors[result['Status']]['meaning'])


        }


        setIsClicked(false)
      })
      .catch((error) => {
        console.error('Error in DNS API call:', error);

        setoutputValue("Network Error")
        setError(false)
        // Handle the error here

      });


      



    } else {
      // Invalid domain, show error message
      setError(true)
      setErrorMessage('Invalid domain name');
      console.log('Invalid domain:', inputValue);
    }

    }



    const handleInputChange = (event) => {
        // Update input when textarea-input changes
        setinputValue(event.target.value)
    }

    const copyBtnRef = useRef(null)
    const [copiedText, setCopiedText] = useState(false)
    const [onHoverActive, setOnHoverActive] = useState(false)

    const handleMouseOver = () => {
        setOnHoverActive(true)
    }
    const handleMouseLeave = () => {
        setOnHoverActive(false)
    }

    const copyToClipboard = () => {
        if (!navigator.clipboard) {
            // Fallback for older browsers (e.g., Internet Explorer)
            const textarea = document.createElement("textarea")
            textarea.value = outputValue
            textarea.style.position = "fixed"
            textarea.style.opacity = 0
            copyBtnRef.current.appendChild(textarea)
            textarea.select()
            document.execCommand("copy")
            copyBtnRef.current.removeChild(textarea)
            return
        }
        navigator.clipboard.writeText(outputValue)
        setCopiedText(true)
        setTimeout(() => {
            setCopiedText(false)
        }, 2000)
    }




    const handlecopy = () => {
        // Your function logic here

        if (!isError && outputValue !== "") {
            clipboardCopy(outputValue)
            console.log("Button clicked!")

            setIsClicked(true)
            setTimeout(() => {
                setIsClicked(false)
            }, 1000)
        }
    }



    const handleSaveToFile = () => {
        if (!isError && outputValue !== "") {
            setIsClicked(true)
            setTimeout(() => {
                setIsClicked(false)
            }, 1000)

            const blob = new Blob([outputValue], { type: "text/plain" })
            const link = document.createElement("a")
            link.href = URL.createObjectURL(blob)
            link.download = "Akto" + props.purpose + ".txt"
            link.click()
        }
    }

    const styles = {
        textboxborder: {
          
            padding: "10px",
            
            borderRadius: "8px",
            border: isError
            ? "2px solid #ff9999"
              : "1px solid #b3b3b3",
              backgroundColor: isError ? "#ff949439" : "",
            
            transition: "border-color 0.5s ease-in-out",
        },
        text: {
            color: isError ? "red" : "green",
        },
        textboxborder2: {
            padding: "20px",
            borderRadius: "8px",
            // border: isClicked ? '2px solid #a366ff':'2px solid #b3b3b3',
            border: "1px solid #b3b3b3",
            fontFamily: 'monospace !important',
          
            transition: "border-color 2s ease-in-out",
            position: "relative",
            zIndex: 0
        },
    }

    const iconStyles = {
        position: "absolute",
        top: "15%",
        right: "10px",
        transform: "translateY(-50%)",
        display: !isError && outputValue !== "" ? "flex" : "none",
        gap: "10px",
    }

    return (
        <div>
            <h1> {props.purpose} </h1>
            <div
                className="Polaris-Card"
                style={{
                    padding: "0px",
                    width: "100%",
                    maxWidth: "100%",
                    fontSize: "16px",
                    borderRadius: "8px",
                    border: "2px solid #E2E1E5",
                }}
            >
                <div
                    style={{ display: "flex", height: "75vh" }}
                    className="main-div"
                >
                    <div
                        style={{
                            flex: "2",
                            flexDirection: "column",
                            gap: "16px",
                            display: "flex",
                            padding: "20px",
                        }}
                        className="editor-div"
                    >
                        <div
                            style={{
                                display: "flex",
                                flexDirection: "column",
                                gap: "6px",
                            }}
                        >
                            <div className="editor">
                                <div className="Polaris-Labelled__LabelWrapper">
                                    <div className="Polaris-Label">
                                        <label className="Polaris-Label__Text">
                                            {" "}
                                            Domain Name{" "}
                                        </label>
                                    </div>
                                </div>

                                <div className="Polaris-Connected">
                                    <div className="Polaris-Connected__Item Polaris-Connected__Item--primary">
                                        <div
                                            className="Polaris-TextField"
                                            
                                        >
                                            <input
                                                value={inputValue}
                                                onChange={handleInputChange}
                                                placeholder={props.regex}
                                                className="Polaris-TextField__Input"
                                                spellCheck="false"
                                                type="text"
                                                style={styles.textboxborder}
                                                autoComplete="off"
                                            />
                                                {" "}

                                                
                                        
                                        </div>

                                        
                <div
                  className="Polaris-Labelled__Error"
                  style={isError ? {} : { visibility: "hidden"}  }
                >
                  <div className="Polaris-InlineError" style={{fontSize:'0.9em'}} >
                    <div className="Polaris-InlineError__Icon">
                      <span className="Polaris-Icon" style={{ fill: "red" }}>
                        <svg
                          viewBox="0 0 20 20"
                          className="Polaris-Icon__Svg"
                          focusable="false"
                          aria-hidden="true"
                        >
                          <path d="M10 6a.75.75 0 0 1 .75.75v3.5a.75.75 0 0 1-1.5 0v-3.5a.75.75 0 0 1 .75-.75Z"></path>
                          <path d="M11 13a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
                          <path
                            fillRule="evenodd"
                            d="M17 10a7 7 0 1 1-14 0 7 7 0 0 1 14 0Zm-1.5 0a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0Z"
                          ></path>
                        </svg>
                      </span>
                    </div>
                    {errMessage}
                  </div>
                  
                </div>
                 

                                    </div>
                                </div>




<div className="">
  <div className="Polaris-Labelled__LabelWrapper">
    <div className="Polaris-Label">
      <label  className="Polaris-Label__Text">Record Type</label>
    </div>
  </div>
  <div className="Polaris-Select">
    <select value={selectedOption} onChange={handleOptionChange} className="Polaris-Select__Input" aria-invalid="false">
    <option value="" disabled>Select an option</option>
    <option value="ALL" >ALL</option>


{Object.keys(DNScodes).map((code) => (
          <option key={uuidv4()} value={code} >
          {DNScodes[code].type} - {DNScodes[code].meaning}
          </option>
        ))}



    </select>
    <div className="Polaris-Select__Content" aria-hidden="true">
      <span className="Polaris-Select__SelectedOption"> {selectedOption} </span>
      <span className="Polaris-Select__Icon">
        <span className="Polaris-Icon">
          <svg viewBox="0 0 20 20" className="Polaris-Icon__Svg" focusable="false" aria-hidden="true">
            <path d="M10.884 4.323a1.25 1.25 0 0 0-1.768 0l-2.646 2.647a.75.75 0 0 0 1.06 1.06l2.47-2.47 2.47 2.47a.75.75 0 1 0 1.06-1.06l-2.646-2.647Z">
            </path>
            <path d="m13.53 13.03-2.646 2.647a1.25 1.25 0 0 1-1.768 0l-2.646-2.647a.75.75 0 0 1 1.06-1.06l2.47 2.47 2.47-2.47a.75.75 0 0 1 1.06 1.06Z">
            </path>
          </svg>
        </span>
      </span>
    </div>
    <div className="Polaris-Select__Backdrop">
    </div>
  </div>
</div>



                          {isClicked ?  
                          <button style={{marginTop:'3px',marginBottom:'10px',width:'100px'}}
                           className="Polaris-Button Polaris-Button--pressable Polaris-Button--variantSecondary Polaris-Button--sizeMedium Polaris-Button--textAlignCenter Polaris-Button--disabled Polaris-Button--loading" 
                           aria-disabled="true" type="button" aria-busy="true" tabIndex="-1">

  <span className="Polaris-Button__Spinner">
    <span className="Polaris-Spinner Polaris-Spinner--sizeSmall">
      <svg viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
        <path d="M7.229 1.173a9.25 9.25 0 1011.655 11.412 1.25 1.25 0 10-2.4-.698 6.75 6.75 0 11-8.506-8.329 1.25 1.25 0 10-.75-2.385z">
        </path>
      </svg>
    </span>
    <span role="status">
      <span className="Polaris-Text--root Polaris-Text--visuallyHidden">Loading</span>
    </span>
  </span>
  
</button> :
                                 
                                <button onClick={handleDNS} style={{backgroundColor: '#6666ff',marginTop:'3px',marginBottom:'10px'}} className="Polaris-Button Polaris-Button--pressable Polaris-Button--variantPrimary Polaris-Button--sizeMedium Polaris-Button--textAlignCenter" type="button">
  <span className="">DNS Lookup</span>
</button>
}            
                                <br />

                                

                                <div className="Polaris-Labelled__LabelWrapper">
                                    <div className="Polaris-Label">
                                        <label className="Polaris-Label__Text">
                                            {" "}
                                            Details{" "}
                                        </label>
                                    </div>
                                </div>

                                <div className="Polaris-Connected">
                                    <div className="Polaris-Connected__Item Polaris-Connected__Item--primary">
                                        <div
                                            className="Polaris-TextField Polaris-TextField--hasValue Polaris-TextField--multiline"
                                         
                                        >
                                            <textarea
                                                multiline="true"
                                                value={outputValue}
                                                placeholder={props.sample_text}
                                                readOnly={true}
                                                className="Polaris-TextField__Input"
                                                spellCheck="false"
                                                type="text"
                                                rows="12"
                                                style={styles.textboxborder2}
                                            ></textarea>
                                            <div style={iconStyles}>
                                                <div
                                                    ref={copyBtnRef}
                                                    onClick={copyToClipboard}
                                                    style={{
                                                        cursor: "pointer",
                                                        display: "flex",
                                                        alignItems: "center",
                                                        padding: "8px 12px",
                                                    }}
                                                    onMouseEnter={
                                                        handleMouseOver
                                                    }
                                                    onMouseLeave={
                                                        handleMouseLeave
                                                    }
                                                >
                                                    <i
                                                        className="fa fa-file fa-2x"
                                                        style={{
                                                            cursor: "pointer",
                                                            fontSize: "20px",
                                                        }}
                                                    ></i>
                                                    {onHoverActive ? (
                                                        <div
                                                            className="Polaris-PositionedOverlay Polaris-Card"
                                                            style={{
                                                                transform: `translate(-30px, -35px)`,
                                                                padding: "8px",
                                                                position:
                                                                    "absolute",
                                                            }}
                                                        >
                                                            {!copiedText
                                                                ? "Copy to clipboard"
                                                                : "Copied!!"}{" "}
                                                        </div>
                                                    ) : null}
                                                </div>
                                            </div>
                                            <div
                                                aria-hidden="true"
                                                className="Polaris-TextField__Resizer"
                                            ></div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div
                    style={{
                        background: "#fafafb",
                        padding: "20px",
                        width: "100%",
                    }}
                >
                    <img
                        src="https://akto-setup.s3.amazonaws.com/templates/128x128.png"
                        alt="Akto.io"
                        style={{ height: "24px" }}
                    />
                </div>
            </div>
        </div>
    )
}

DomainTools.defaultProps = {
    purpose: "DNSLookup",
    regex: "www.example.com",
    sample_text: "DNS lookup details goes here...",
}

// addPropertyControls(DomainTools, {
//     purpose: { type: ControlType.String, title: "Purpose" },
//     regex: { type: ControlType.String, title: "Regex" },
//     sample_text: { type: ControlType.String, title: "Sample text" },
// })