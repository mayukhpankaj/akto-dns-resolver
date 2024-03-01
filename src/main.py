from bs4 import BeautifulSoup
import csv

# Your HTML content
html_content = """
<!-- Your HTML content goes here -->

<tbody><tr>
            <td>Reserved</td>
            <td align="center">0</td>
            <td></td>
            <td>[<a href="https://www.iana.org/go/rfc6895">RFC6895</a>]</td>
            <td></td>
            <td>2021-03-08</td>
          </tr><tr>
            <td>A</td>
            <td align="center">1</td>
            <td>a host address</td>
            <td>[<a href="https://www.iana.org/go/rfc1035">RFC1035</a>]</td>
            <td></td>
            <td></td>
          </tr><tr>
            <td>NS</td>
            <td align="center">2</td>
            <td>an authoritative name server</td>
            <td>[<a href="https://www.iana.org/go/rfc1035">RFC1035</a>]</td>
            <td></td>
            <td></td>
          </tr><tr>
            <td>MD</td>
            <td align="center">3</td>
            <td>a mail destination (OBSOLETE - use MX)</td>
            <td>[<a href="https://www.iana.org/go/rfc1035">RFC1035</a>]</td>
            <td></td>
            <td></td>
          </tr><tr>
            <td>MF</td>
            <td align="center">4</td>
            <td>a mail forwarder (OBSOLETE - use MX)</td>
            <td>[<a href="https://www.iana.org/go/rfc1035">RFC1035</a>]</td>
            <td></td>
            <td></td>
          </tr><tr>
            <td>CNAME</td>
            <td align="center">5</td>
            <td>the canonical name for an alias</td>
            <td>[<a href="https://www.iana.org/go/rfc1035">RFC1035</a>]</td>
            <td></td>
            <td></td>
          </tr><tr>
            <td>SOA</td>
            <td align="center">6</td>
            <td>marks the start of a zone of authority</td>
            <td>[<a href="https://www.iana.org/go/rfc1035">RFC1035</a>]</td>
            <td></td>
            <td></td>
          </tr><tr>
            <td>MB</td>
            <td align="center">7</td>
            <td>a mailbox domain name (EXPERIMENTAL)</td>
            <td>[<a href="https://www.iana.org/go/rfc1035">RFC1035</a>]</td>
            <td></td>
            <td></td>
          </tr><tr>
            <td>MG</td>
            <td align="center">8</td>
            <td>a mail group member (EXPERIMENTAL)</td>
            <td>[<a href="https://www.iana.org/go/rfc1035">RFC1035</a>]</td>
            <td></td>
            <td></td>
          </tr><tr>
            <td>MR</td>
            <td align="center">9</td>
            <td>a mail rename domain name (EXPERIMENTAL)</td>
            <td>[<a href="https://www.iana.org/go/rfc1035">RFC1035</a>]</td>
            <td></td>
            <td></td>
          </tr><tr>
            <td>NULL</td>
            <td align="center">10</td>
            <td>a null RR (EXPERIMENTAL)</td>
            <td>[<a href="https://www.iana.org/go/rfc1035">RFC1035</a>]</td>
            <td></td>
            <td></td>
          </tr><tr>
            <td>WKS</td>
            <td align="center">11</td>
            <td>a well known service description</td>
            <td>[<a href="https://www.iana.org/go/rfc1035">RFC1035</a>]</td>
            <td></td>
            <td></td>
          </tr><tr>
            <td>PTR</td>
            <td align="center">12</td>
            <td>a domain name pointer</td>
            <td>[<a href="https://www.iana.org/go/rfc1035">RFC1035</a>]</td>
            <td></td>
            <td></td>
          </tr><tr>
            <td>HINFO</td>
            <td align="center">13</td>
            <td>host information</td>
            <td>[<a href="https://www.iana.org/go/rfc1035">RFC1035</a>]</td>
            <td></td>
            <td></td>
          </tr><tr>
            <td>MINFO</td>
            <td align="center">14</td>
            <td>mailbox or mail list information</td>
            <td>[<a href="https://www.iana.org/go/rfc1035">RFC1035</a>]</td>
            <td></td>
            <td></td>
          </tr><tr>
            <td>MX</td>
            <td align="center">15</td>
            <td>mail exchange</td>
            <td>[<a href="https://www.iana.org/go/rfc1035">RFC1035</a>]</td>
            <td></td>
            <td></td>
          </tr><tr>
            <td>TXT</td>
            <td align="center">16</td>
            <td>text strings</td>
            <td>[<a href="https://www.iana.org/go/rfc1035">RFC1035</a>]</td>
            <td></td>
            <td></td>
          </tr><tr>
            <td>RP</td>
            <td align="center">17</td>
            <td>for Responsible Person</td>
            <td>[<a href="https://www.iana.org/go/rfc1183">RFC1183</a>]</td>
            <td></td>
            <td></td>
          </tr><tr>
            <td>AFSDB</td>
            <td align="center">18</td>
            <td>for AFS Data Base location</td>
            <td>[<a href="https://www.iana.org/go/rfc1183">RFC1183</a>][<a href="https://www.iana.org/go/rfc5864">RFC5864</a>]</td>
            <td></td>
            <td></td>
          </tr><tr>
            <td>X25</td>
            <td align="center">19</td>
            <td>for X.25 PSDN address</td>
            <td>[<a href="https://www.iana.org/go/rfc1183">RFC1183</a>]</td>
            <td></td>
            <td></td>
          </tr><tr>
            <td>ISDN</td>
            <td align="center">20</td>
            <td>for ISDN address</td>
            <td>[<a href="https://www.iana.org/go/rfc1183">RFC1183</a>]</td>
            <td></td>
            <td></td>
          </tr><tr>
            <td>RT</td>
            <td align="center">21</td>
            <td>for Route Through</td>
            <td>[<a href="https://www.iana.org/go/rfc1183">RFC1183</a>]</td>
            <td></td>
            <td></td>
          </tr><tr>
            <td>NSAP</td>
            <td align="center">22</td>
            <td>for NSAP address, NSAP style A record (DEPRECATED)</td>
            <td>[<a href="https://www.iana.org/go/rfc1706">RFC1706</a>][<a href="https://datatracker.ietf.org/doc/status-change-int-tlds-to-historic">status-change-int-tlds-to-historic</a>]</td>
            <td></td>
            <td></td>
          </tr><tr>
            <td>NSAP-PTR</td>
            <td align="center">23</td>
            <td>for domain name pointer, NSAP style (DEPRECATED)</td>
            <td>[<a href="https://www.iana.org/go/rfc1706">RFC1706</a>][<a href="https://datatracker.ietf.org/doc/status-change-int-tlds-to-historic">status-change-int-tlds-to-historic</a>]</td>
            <td></td>
            <td></td>
          </tr><tr>
            <td>SIG</td>
            <td align="center">24</td>
            <td>for security signature</td>
            <td>[<a href="https://www.iana.org/go/rfc2536">RFC2536</a>][<a href="https://www.iana.org/go/rfc2931">RFC2931</a>][<a href="https://www.iana.org/go/rfc3110">RFC3110</a>][<a href="https://www.iana.org/go/rfc4034">RFC4034</a>]</td>
            <td></td>
            <td></td>
          </tr><tr>
            <td>KEY</td>
            <td align="center">25</td>
            <td>for security key</td>
            <td>[<a href="https://www.iana.org/go/rfc2536">RFC2536</a>][<a href="https://www.iana.org/go/rfc2539">RFC2539</a>][<a href="https://www.iana.org/go/rfc3110">RFC3110</a>][<a href="https://www.iana.org/go/rfc4034">RFC4034</a>]</td>
            <td></td>
            <td></td>
          </tr><tr>
            <td>PX</td>
            <td align="center">26</td>
            <td>X.400 mail mapping information</td>
            <td>[<a href="https://www.iana.org/go/rfc2163">RFC2163</a>]</td>
            <td></td>
            <td></td>
          </tr><tr>
            <td>GPOS</td>
            <td align="center">27</td>
            <td>Geographical Position</td>
            <td>[<a href="https://www.iana.org/go/rfc1712">RFC1712</a>]</td>
            <td></td>
            <td></td>
          </tr><tr>
            <td>AAAA</td>
            <td align="center">28</td>
            <td>IP6 Address</td>
            <td>[<a href="https://www.iana.org/go/rfc3596">RFC3596</a>]</td>
            <td></td>
            <td></td>
          </tr><tr>
            <td>LOC</td>
            <td align="center">29</td>
            <td>Location Information</td>
            <td>[<a href="https://www.iana.org/go/rfc1876">RFC1876</a>]</td>
            <td></td>
            <td></td>
          </tr><tr>
            <td>NXT</td>
            <td align="center">30</td>
            <td>Next Domain (OBSOLETE)</td>
            <td>[<a href="https://www.iana.org/go/rfc2535">RFC2535</a>][<a href="https://www.iana.org/go/rfc3755">RFC3755</a>]</td>
            <td></td>
            <td></td>
          </tr><tr>
            <td>EID</td>
            <td align="center">31</td>
            <td>Endpoint Identifier</td>
            <td>[<a href="#Michael_Patton">Michael_Patton</a>][<a href="http://ana-3.lcs.mit.edu/~jnc/nimrod/dns.txt">http://ana-3.lcs.mit.edu/~jnc/nimrod/dns.txt</a>]</td>
            <td></td>
            <td>1995-06</td>
          </tr><tr>
            <td>NIMLOC</td>
            <td align="center">32</td>
            <td>Nimrod Locator</td>
            <td>[<a href="#note1">1</a>][<a href="#Michael_Patton">Michael_Patton</a>][<a href="http://ana-3.lcs.mit.edu/~jnc/nimrod/dns.txt">http://ana-3.lcs.mit.edu/~jnc/nimrod/dns.txt</a>]</td>
            <td></td>
            <td>1995-06</td>
          </tr><tr>
            <td>SRV</td>
            <td align="center">33</td>
            <td>Server Selection</td>
            <td>[<a href="#note1">1</a>][<a href="https://www.iana.org/go/rfc2782">RFC2782</a>]</td>
            <td></td>
            <td></td>
          </tr><tr>
            <td>ATMA</td>
            <td align="center">34</td>
            <td>ATM Address</td>
            <td>[<a href="http://www.broadband-forum.org/ftp/pub/approved-specs/af-dans-0152.000.pdf">
        ATM Forum Technical Committee, "ATM Name System, V2.0", Doc ID: AF-DANS-0152.000, July 2000. Available from and held in escrow by IANA.</a>]</td>
            <td></td>
            <td></td>
          </tr><tr>
            <td>NAPTR</td>
            <td align="center">35</td>
            <td>Naming Authority Pointer</td>
            <td>[<a href="https://www.iana.org/go/rfc3403">RFC3403</a>]</td>
            <td></td>
            <td></td>
          </tr><tr>
            <td>KX</td>
            <td align="center">36</td>
            <td>Key Exchanger</td>
            <td>[<a href="https://www.iana.org/go/rfc2230">RFC2230</a>]</td>
            <td></td>
            <td></td>
          </tr><tr>
            <td>CERT</td>
            <td align="center">37</td>
            <td>CERT</td>
            <td>[<a href="https://www.iana.org/go/rfc4398">RFC4398</a>]</td>
            <td></td>
            <td></td>
          </tr><tr>
            <td>A6</td>
            <td align="center">38</td>
            <td>A6 (OBSOLETE - use AAAA)</td>
            <td>[<a href="https://www.iana.org/go/rfc2874">RFC2874</a>][<a href="https://www.iana.org/go/rfc3226">RFC3226</a>][<a href="https://www.iana.org/go/rfc6563">RFC6563</a>]</td>
            <td></td>
            <td></td>
          </tr><tr>
            <td>DNAME</td>
            <td align="center">39</td>
            <td>DNAME</td>
            <td>[<a href="https://www.iana.org/go/rfc6672">RFC6672</a>]</td>
            <td></td>
            <td></td>
          </tr><tr>
            <td>SINK</td>
            <td align="center">40</td>
            <td>SINK</td>
            <td>[<a href="#Donald_E_Eastlake">Donald_E_Eastlake</a>][<a href="https://www.iana.org/go/draft-eastlake-kitchen-sink">draft-eastlake-kitchen-sink</a>]</td>
            <td></td>
            <td>1997-11</td>
          </tr><tr>
            <td>OPT</td>
            <td align="center">41</td>
            <td>OPT</td>
            <td>[<a href="https://www.iana.org/go/rfc3225">RFC3225</a>][<a href="https://www.iana.org/go/rfc6891">RFC6891</a>]</td>
            <td></td>
            <td></td>
          </tr><tr>
            <td>APL</td>
            <td align="center">42</td>
            <td>APL</td>
            <td>[<a href="https://www.iana.org/go/rfc3123">RFC3123</a>]</td>
            <td></td>
            <td></td>
          </tr><tr>
            <td>DS</td>
            <td align="center">43</td>
            <td>Delegation Signer</td>
            <td>[<a href="https://www.iana.org/go/rfc4034">RFC4034</a>]</td>
            <td></td>
            <td></td>
          </tr><tr>
            <td>SSHFP</td>
            <td align="center">44</td>
            <td>SSH Key Fingerprint</td>
            <td>[<a href="https://www.iana.org/go/rfc4255">RFC4255</a>]</td>
            <td></td>
            <td></td>
          </tr><tr>
            <td>IPSECKEY</td>
            <td align="center">45</td>
            <td>IPSECKEY</td>
            <td>[<a href="https://www.iana.org/go/rfc4025">RFC4025</a>]</td>
            <td></td>
            <td></td>
          </tr><tr>
            <td>RRSIG</td>
            <td align="center">46</td>
            <td>RRSIG</td>
            <td>[<a href="https://www.iana.org/go/rfc4034">RFC4034</a>]</td>
            <td></td>
            <td></td>
          </tr><tr>
            <td>NSEC</td>
            <td align="center">47</td>
            <td>NSEC</td>
            <td>[<a href="https://www.iana.org/go/rfc4034">RFC4034</a>][<a href="https://www.iana.org/go/rfc9077">RFC9077</a>]</td>
            <td></td>
            <td></td>
          </tr><tr>
            <td>DNSKEY</td>
            <td align="center">48</td>
            <td>DNSKEY</td>
            <td>[<a href="https://www.iana.org/go/rfc4034">RFC4034</a>]</td>
            <td></td>
            <td></td>
          </tr><tr>
            <td>DHCID</td>
            <td align="center">49</td>
            <td>DHCID</td>
            <td>[<a href="https://www.iana.org/go/rfc4701">RFC4701</a>]</td>
            <td></td>
            <td></td>
          </tr><tr>
            <td>NSEC3</td>
            <td align="center">50</td>
            <td>NSEC3</td>
            <td>[<a href="https://www.iana.org/go/rfc5155">RFC5155</a>][<a href="https://www.iana.org/go/rfc9077">RFC9077</a>]</td>
            <td></td>
            <td></td>
          </tr><tr>
            <td>NSEC3PARAM</td>
            <td align="center">51</td>
            <td>NSEC3PARAM</td>
            <td>[<a href="https://www.iana.org/go/rfc5155">RFC5155</a>]</td>
            <td></td>
            <td></td>
          </tr><tr>
            <td>TLSA</td>
            <td align="center">52</td>
            <td>TLSA</td>
            <td>[<a href="https://www.iana.org/go/rfc6698">RFC6698</a>]</td>
            <td></td>
            <td></td>
          </tr><tr>
            <td>SMIMEA</td>
            <td align="center">53</td>
            <td>S/MIME cert association</td>
            <td>[<a href="https://www.iana.org/go/rfc8162">RFC8162</a>]</td>
            <td>
              <a href="SMIMEA/smimea-completed-template">SMIMEA/smimea-completed-template</a>
            </td>
            <td>2015-12-01</td>
          </tr><tr>
            <td>Unassigned</td>
            <td align="center">54</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
          </tr><tr>
            <td>HIP</td>
            <td align="center">55</td>
            <td>Host Identity Protocol</td>
            <td>[<a href="https://www.iana.org/go/rfc8005">RFC8005</a>]</td>
            <td></td>
            <td></td>
          </tr><tr>
            <td>NINFO</td>
            <td align="center">56</td>
            <td>NINFO</td>
            <td>[<a href="#Jim_Reid">Jim_Reid</a>]</td>
            <td>
              <a href="NINFO/ninfo-completed-template">NINFO/ninfo-completed-template</a>
            </td>
            <td>2008-01-21</td>
          </tr><tr>
            <td>RKEY</td>
            <td align="center">57</td>
            <td>RKEY</td>
            <td>[<a href="#Jim_Reid">Jim_Reid</a>]</td>
            <td>
              <a href="RKEY/rkey-completed-template">RKEY/rkey-completed-template</a>
            </td>
            <td>2008-01-21</td>
          </tr><tr>
            <td>TALINK</td>
            <td align="center">58</td>
            <td>Trust Anchor LINK</td>
            <td>[<a href="#Wouter_Wijngaards">Wouter_Wijngaards</a>]</td>
            <td>
              <a href="TALINK/talink-completed-template">TALINK/talink-completed-template</a>
            </td>
            <td>2010-02-17</td>
          </tr><tr>
            <td>CDS</td>
            <td align="center">59</td>
            <td>Child DS</td>
            <td>[<a href="https://www.iana.org/go/rfc7344">RFC7344</a>]</td>
            <td>
              <a href="CDS/cds-completed-template">CDS/cds-completed-template</a>
            </td>
            <td>2011-06-06</td>
          </tr><tr>
            <td>CDNSKEY</td>
            <td align="center">60</td>
            <td>DNSKEY(s) the Child wants reflected in DS</td>
            <td>[<a href="https://www.iana.org/go/rfc7344">RFC7344</a>]</td>
            <td></td>
            <td>2014-06-16</td>
          </tr><tr>
            <td>OPENPGPKEY</td>
            <td align="center">61</td>
            <td>OpenPGP Key</td>
            <td>[<a href="https://www.iana.org/go/rfc7929">RFC7929</a>]</td>
            <td>
              <a href="OPENPGPKEY/openpgpkey-completed-template">OPENPGPKEY/openpgpkey-completed-template</a>
            </td>
            <td>2014-08-12</td>
          </tr><tr>
            <td>CSYNC</td>
            <td align="center">62</td>
            <td>Child-To-Parent Synchronization</td>
            <td>[<a href="https://www.iana.org/go/rfc7477">RFC7477</a>]</td>
            <td></td>
            <td>2015-01-27</td>
          </tr><tr>
            <td>ZONEMD</td>
            <td align="center">63</td>
            <td>Message Digest Over Zone Data</td>
            <td>[<a href="https://www.iana.org/go/rfc8976">RFC8976</a>]</td>
            <td>
              <a href="ZONEMD/zonemd-completed-template">ZONEMD/zonemd-completed-template</a>
            </td>
            <td>2018-12-12</td>
          </tr><tr>
            <td>SVCB</td>
            <td align="center">64</td>
            <td>General-purpose service binding</td>
            <td>[<a href="https://www.iana.org/go/rfc9460">RFC9460</a>]</td>
            <td>
              <a href="SVCB/svcb-completed-template">SVCB/svcb-completed-template</a>
            </td>
            <td>2020-06-30</td>
          </tr><tr>
            <td>HTTPS</td>
            <td align="center">65</td>
            <td>SVCB-compatible type for use with HTTP</td>
            <td>[<a href="https://www.iana.org/go/rfc9460">RFC9460</a>]</td>
            <td>
              <a href="HTTPS/https-completed-template">HTTPS/https-completed-template</a>
            </td>
            <td>2020-06-30</td>
          </tr><tr>
            <td>Unassigned</td>
            <td align="center">66-98</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
          </tr><tr>
            <td>SPF</td>
            <td align="center">99</td>
            <td></td>
            <td>[<a href="https://www.iana.org/go/rfc7208">RFC7208</a>]</td>
            <td></td>
            <td></td>
          </tr><tr>
            <td>UINFO</td>
            <td align="center">100</td>
            <td></td>
            <td>[IANA-Reserved]</td>
            <td></td>
            <td></td>
          </tr><tr>
            <td>UID</td>
            <td align="center">101</td>
            <td></td>
            <td>[IANA-Reserved]</td>
            <td></td>
            <td></td>
          </tr><tr>
            <td>GID</td>
            <td align="center">102</td>
            <td></td>
            <td>[IANA-Reserved]</td>
            <td></td>
            <td></td>
          </tr><tr>
            <td>UNSPEC</td>
            <td align="center">103</td>
            <td></td>
            <td>[IANA-Reserved]</td>
            <td></td>
            <td></td>
          </tr><tr>
            <td>NID</td>
            <td align="center">104</td>
            <td></td>
            <td>[<a href="https://www.iana.org/go/rfc6742">RFC6742</a>]</td>
            <td>
              <a href="ILNP/nid-completed-template">ILNP/nid-completed-template</a>
            </td>
            <td></td>
          </tr><tr>
            <td>L32</td>
            <td align="center">105</td>
            <td></td>
            <td>[<a href="https://www.iana.org/go/rfc6742">RFC6742</a>]</td>
            <td>
              <a href="ILNP/l32-completed-template">ILNP/l32-completed-template</a>
            </td>
            <td></td>
          </tr><tr>
            <td>L64</td>
            <td align="center">106</td>
            <td></td>
            <td>[<a href="https://www.iana.org/go/rfc6742">RFC6742</a>]</td>
            <td>
              <a href="ILNP/l64-completed-template">ILNP/l64-completed-template</a>
            </td>
            <td></td>
          </tr><tr>
            <td>LP</td>
            <td align="center">107</td>
            <td></td>
            <td>[<a href="https://www.iana.org/go/rfc6742">RFC6742</a>]</td>
            <td>
              <a href="ILNP/lp-completed-template">ILNP/lp-completed-template</a>
            </td>
            <td></td>
          </tr><tr>
            <td>EUI48</td>
            <td align="center">108</td>
            <td>an EUI-48 address</td>
            <td>[<a href="https://www.iana.org/go/rfc7043">RFC7043</a>]</td>
            <td>
              <a href="EUI48/eui48-completed-template">EUI48/eui48-completed-template</a>
            </td>
            <td>2013-03-27</td>
          </tr><tr>
            <td>EUI64</td>
            <td align="center">109</td>
            <td>an EUI-64 address</td>
            <td>[<a href="https://www.iana.org/go/rfc7043">RFC7043</a>]</td>
            <td>
              <a href="EUI64/eui64-completed-template">EUI64/eui64-completed-template</a>
            </td>
            <td>2013-03-27</td>
          </tr><tr>
            <td>Unassigned</td>
            <td align="center">110-248</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
          </tr><tr>
            <td>TKEY</td>
            <td align="center">249</td>
            <td>Transaction Key</td>
            <td>[<a href="https://www.iana.org/go/rfc2930">RFC2930</a>]</td>
            <td></td>
            <td></td>
          </tr><tr>
            <td>TSIG</td>
            <td align="center">250</td>
            <td>Transaction Signature</td>
            <td>[<a href="https://www.iana.org/go/rfc8945">RFC8945</a>]</td>
            <td></td>
            <td></td>
          </tr><tr>
            <td>IXFR</td>
            <td align="center">251</td>
            <td>incremental transfer</td>
            <td>[<a href="https://www.iana.org/go/rfc1995">RFC1995</a>]</td>
            <td></td>
            <td></td>
          </tr><tr>
            <td>AXFR</td>
            <td align="center">252</td>
            <td>transfer of an entire zone</td>
            <td>[<a href="https://www.iana.org/go/rfc1035">RFC1035</a>][<a href="https://www.iana.org/go/rfc5936">RFC5936</a>]</td>
            <td></td>
            <td></td>
          </tr><tr>
            <td>MAILB</td>
            <td align="center">253</td>
            <td>mailbox-related RRs (MB, MG or MR)</td>
            <td>[<a href="https://www.iana.org/go/rfc1035">RFC1035</a>]</td>
            <td></td>
            <td></td>
          </tr><tr>
            <td>MAILA</td>
            <td align="center">254</td>
            <td>mail agent RRs (OBSOLETE - see MX)</td>
            <td>[<a href="https://www.iana.org/go/rfc1035">RFC1035</a>]</td>
            <td></td>
            <td></td>
          </tr><tr>
            <td>*</td>
            <td align="center">255</td>
            <td>A request for some or all records the server has available</td>
            <td>[<a href="https://www.iana.org/go/rfc1035">RFC1035</a>][<a href="https://www.iana.org/go/rfc6895">RFC6895</a>][<a href="https://www.iana.org/go/rfc8482">RFC8482</a>]</td>
            <td></td>
            <td></td>
          </tr><tr>
            <td>URI</td>
            <td align="center">256</td>
            <td>URI</td>
            <td>[<a href="https://www.iana.org/go/rfc7553">RFC7553</a>]</td>
            <td>
              <a href="URI/uri-completed-template">URI/uri-completed-template</a>
            </td>
            <td>2011-02-22</td>
          </tr><tr>
            <td>CAA</td>
            <td align="center">257</td>
            <td>Certification Authority Restriction</td>
            <td>[<a href="https://www.iana.org/go/rfc8659">RFC8659</a>]</td>
            <td>
              <a href="CAA/caa-completed-template">CAA/caa-completed-template</a>
            </td>
            <td>2011-04-07</td>
          </tr><tr>
            <td>AVC</td>
            <td align="center">258</td>
            <td>Application Visibility and Control</td>
            <td>[<a href="#Wolfgang_Riedel">Wolfgang_Riedel</a>]</td>
            <td>
              <a href="AVC/avc-completed-template">AVC/avc-completed-template</a>
            </td>
            <td>2016-02-26</td>
          </tr><tr>
            <td>DOA</td>
            <td align="center">259</td>
            <td>Digital Object Architecture</td>
            <td>[<a href="https://www.iana.org/go/draft-durand-doa-over-dns">draft-durand-doa-over-dns</a>]</td>
            <td>
              <a href="DOA/doa-completed-template">DOA/doa-completed-template</a>
            </td>
            <td>2017-08-30</td>
          </tr><tr>
            <td>AMTRELAY</td>
            <td align="center">260</td>
            <td>Automatic Multicast Tunneling Relay</td>
            <td>[<a href="https://www.iana.org/go/rfc8777">RFC8777</a>]</td>
            <td>
              <a href="AMTRELAY/amtrelay-completed-template">AMTRELAY/amtrelay-completed-template</a>
            </td>
            <td>2019-02-06</td>
          </tr><tr>
            <td>RESINFO</td>
            <td align="center">261</td>
            <td>Resolver Information as Key/Value Pairs</td>
            <td>[<a href="https://www.iana.org/go/draft-ietf-add-resolver-info-06">draft-ietf-add-resolver-info-06</a>]</td>
            <td>
              <a href="RESINFO/resinfo-completed-template">RESINFO/resinfo-completed-template</a>
            </td>
            <td>2023-11-02</td>
          </tr><tr>
            <td>Unassigned</td>
            <td align="center">262-32767</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
          </tr><tr>
            <td>TA</td>
            <td align="center">32768</td>
            <td>DNSSEC Trust Authorities</td>
            <td>[<a href="#Sam_Weiler">Sam_Weiler</a>][<a href="http://cameo.library.cmu.edu/">http://cameo.library.cmu.edu/</a>][<a href="http://www.watson.org/~weiler/INI1999-19.pdf">
        Deploying DNSSEC Without a Signed Root.  Technical Report 1999-19,
Information Networking Institute, Carnegie Mellon University, April 2004.</a>]</td>
            <td></td>
            <td>2005-12-13</td>
          </tr><tr>
            <td>DLV</td>
            <td align="center">32769</td>
            <td>DNSSEC Lookaside Validation (OBSOLETE)</td>
            <td>[<a href="https://www.iana.org/go/rfc8749">RFC8749</a>][<a href="https://www.iana.org/go/rfc4431">RFC4431</a>]</td>
            <td></td>
            <td></td>
          </tr><tr>
            <td>Unassigned</td>
            <td align="center">32770-65279</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
          </tr><tr>
            <td>Private use</td>
            <td align="center">65280-65534</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
          </tr><tr>
            <td>Reserved</td>
            <td align="center">65535</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
          </tr></tbody>
"""

# Parse HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find all table rows
rows = soup.find_all('tr')

# Process each row
for row in rows:
    # Find all table data in the row
    tds = row.find_all('td')

    # Check if there are more than 3 td elements
    if len(tds) > 3:
        # Remove all td elements after the first 3
        for td in tds[3:]:
            td.decompose()

# Get the modified HTML content
# modified_html = str(soup)

# file_path = './file.html'

# with open(file_path, 'w', encoding='utf-8') as file:
#     file.write(soup)

# # Print or use the modified HTML content as needed
# print(modified_html)
            table = soup.find('tbody')

            
csv_file_path = './table_data.csv'

with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)


    # Write each row to the CSV
    for row in table.find_all('tr'):
        csv_row = [data.text.strip() for data in row.find_all('td')]
        csv_writer.writerow(csv_row)

print(f'Table data saved to {csv_file_path} in CSV format.')

