import React from "react";
import DomainTools from "./DomainTools";
import ReverseIP from "./ReverseIP";
import CnameLookup from './CnameLookup.jsx'

export default function App() {


  return (
    <div>
      {/* <DomainTools purpose="DNSLookup" /> */}
      {/* <ReverseIP purpose="Reverse Ip" /> */}
      <CnameLookup />

    </div>
  );
}