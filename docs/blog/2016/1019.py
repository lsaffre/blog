import bleach
import lino

lino.startup('lino_noi.projects.team.settings.demo')

from etgen.html import E
from lino.modlib.memo.mixins import rich_text_to_elems
from lino.api import rt

body = u'<p><!--[if gte mso 9]><xml>\n <o:OfficeDocumentSettings>\n  <o:AllowPNG/>\n </o:OfficeDocumentSettings>\n</xml><![endif]--></p>\n<p><!--[if gte mso 9]><xml>\n <w:WordDocument>\n  <w:View>Normal</w:View>\n  <w:Zoom>0</w:Zoom>\n  <w:TrackMoves/>\n  <w:TrackFormatting/>\n  <w:HyphenationZone>21</w:HyphenationZone>\n  <w:PunctuationKerning/>\n  <w:ValidateAgainstSchemas/>\n  <w:SaveIfXMLInvalid>false</w:SaveIfXMLInvalid>\n  <w:IgnoreMixedContent>false</w:IgnoreMixedContent>\n  <w:AlwaysShowPlaceholderText>false</w:AlwaysShowPlaceholderText>\n  <w:DoNotPromoteQF/>\n  <w:LidThemeOther>FR-BE</w:LidThemeOther>\n  <w:LidThemeAsian>X-NONE</w:LidThemeAsian>\n  <w:LidThemeComplexScript>X-NONE</w:LidThemeComplexScript>\n  <w:Compatibility>\n   <w:BreakWrappedTables/>\n   <w:SnapToGridInCell/>\n   <w:WrapTextWithPunct/>\n   <w:UseAsianBreakRules/>\n   <w:DontGrowAutofit/>\n   <w:SplitPgBreakAndParaMark/>\n   <w:EnableOpenTypeKerning/>\n   <w:DontFlipMirrorIndents/>\n   <w:OverrideTableStyleHps/>\n  </w:Compatibility>\n  <m:mathPr>\n   <m:mathFont m:val="Cambria Math"/>\n   <m:brkBin m:val="before"/>\n   <m:brkBinSub m:val="&#45;-"/>\n   <m:smallFrac m:val="off"/>\n   <m:dispDef/>\n   <m:lMargin m:val="0"/>\n   <m:rMargin m:val="0"/>\n   <m:defJc m:val="centerGroup"/>\n   <m:wrapIndent m:val="1440"/>\n   <m:intLim m:val="subSup"/>\n   <m:naryLim m:val="undOvr"/>\n  </m:mathPr></w:WordDocument>\n</xml><![endif]--><!--[if gte mso 9]><xml>\n <w:LatentStyles DefLockedState="false" DefUnhideWhenUsed="true"\n  DefSemiHidden="true" DefQFormat="false" DefPriority="99"\n  LatentStyleCount="267">\n  <w:LsdException Locked="false" Priority="0" SemiHidden="false"\n   UnhideWhenUsed="false" QFormat="true" Name="Normal"/>\n  <w:LsdException Locked="false" Priority="9" SemiHidden="false"\n   UnhideWhenUsed="false" QFormat="true" Name="heading 1"/>\n  <w:LsdException Locked="false" Priority="9" QFormat="true" Name="heading 2"/>\n  <w:LsdException Locked="false" Priority="9" QFormat="true" Name="heading 3"/>\n  <w:LsdException Locked="false" Priority="9" QFormat="true" Name="heading 4"/>\n  <w:LsdException Locked="false" Priority="9" QFormat="true" Name="heading 5"/>\n  <w:LsdException Locked="false" Priority="9" QFormat="true" Name="heading 6"/>\n  <w:LsdException Locked="false" Priority="9" QFormat="true" Name="heading 7"/>\n  <w:LsdException Locked="false" Priority="9" QFormat="true" Name="heading 8"/>\n  <w:LsdException Locked="false" Priority="9" QFormat="true" Name="heading 9"/>\n  <w:LsdException Locked="false" Priority="39" Name="toc 1"/>\n  <w:LsdException Locked="false" Priority="39" Name="toc 2"/>\n  <w:LsdException Locked="false" Priority="39" Name="toc 3"/>\n  <w:LsdException Locked="false" Priority="39" Name="toc 4"/>\n  <w:LsdException Locked="false" Priority="39" Name="toc 5"/>\n  <w:LsdException Locked="false" Priority="39" Name="toc 6"/>\n  <w:LsdException Locked="false" Priority="39" Name="toc 7"/>\n  <w:LsdException Locked="false" Priority="39" Name="toc 8"/>\n  <w:LsdException Locked="false" Priority="39" Name="toc 9"/>\n  <w:LsdException Locked="false" Priority="35" QFormat="true" Name="caption"/>\n  <w:LsdException Locked="false" Priority="10" SemiHidden="false"\n   UnhideWhenUsed="false" QFormat="true" Name="Title"/>\n  <w:LsdException Locked="false" Priority="1" Name="Default Paragraph Font"/>\n  <w:LsdException Locked="false" Priority="11" SemiHidden="false"\n   UnhideWhenUsed="false" QFormat="true" Name="Subtitle"/>\n  <w:LsdException Locked="false" Priority="22" SemiHidden="false"\n   UnhideWhenUsed="false" QFormat="true" Name="Strong"/>\n  <w:LsdException Locked="false" Priority="20" SemiHidden="false"\n   UnhideWhenUsed="false" QFormat="true" Name="Emphasis"/>\n  <w:LsdException Locked="false" Priority="59" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Table Grid"/>\n  <w:LsdException Locked="false" UnhideWhenUsed="false" Name="Placeholder Text"/>\n  <w:LsdException Locked="false" Priority="1" SemiHidden="false"\n   UnhideWhenUsed="false" QFormat="true" Name="No Spacing"/>\n  <w:LsdException Locked="false" Priority="60" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Light Shading"/>\n  <w:LsdException Locked="false" Priority="61" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Light List"/>\n  <w:LsdException Locked="false" Priority="62" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Light Grid"/>\n  <w:LsdException Locked="false" Priority="63" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Medium Shading 1"/>\n  <w:LsdException Locked="false" Priority="64" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Medium Shading 2"/>\n  <w:LsdException Locked="false" Priority="65" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Medium List 1"/>\n  <w:LsdException Locked="false" Priority="66" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Medium List 2"/>\n  <w:LsdException Locked="false" Priority="67" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Medium Grid 1"/>\n  <w:LsdException Locked="false" Priority="68" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Medium Grid 2"/>\n  <w:LsdException Locked="false" Priority="69" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Medium Grid 3"/>\n  <w:LsdException Locked="false" Priority="70" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Dark List"/>\n  <w:LsdException Locked="false" Priority="71" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Colorful Shading"/>\n  <w:LsdException Locked="false" Priority="72" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Colorful List"/>\n  <w:LsdException Locked="false" Priority="73" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Colorful Grid"/>\n  <w:LsdException Locked="false" Priority="60" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Light Shading Accent 1"/>\n  <w:LsdException Locked="false" Priority="61" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Light List Accent 1"/>\n  <w:LsdException Locked="false" Priority="62" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Light Grid Accent 1"/>\n  <w:LsdException Locked="false" Priority="63" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Medium Shading 1 Accent 1"/>\n  <w:LsdException Locked="false" Priority="64" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Medium Shading 2 Accent 1"/>\n  <w:LsdException Locked="false" Priority="65" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Medium List 1 Accent 1"/>\n  <w:LsdException Locked="false" UnhideWhenUsed="false" Name="Revision"/>\n  <w:LsdException Locked="false" Priority="34" SemiHidden="false"\n   UnhideWhenUsed="false" QFormat="true" Name="List Paragraph"/>\n  <w:LsdException Locked="false" Priority="29" SemiHidden="false"\n   UnhideWhenUsed="false" QFormat="true" Name="Quote"/>\n  <w:LsdException Locked="false" Priority="30" SemiHidden="false"\n   UnhideWhenUsed="false" QFormat="true" Name="Intense Quote"/>\n  <w:LsdException Locked="false" Priority="66" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Medium List 2 Accent 1"/>\n  <w:LsdException Locked="false" Priority="67" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Medium Grid 1 Accent 1"/>\n  <w:LsdException Locked="false" Priority="68" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Medium Grid 2 Accent 1"/>\n  <w:LsdException Locked="false" Priority="69" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Medium Grid 3 Accent 1"/>\n  <w:LsdException Locked="false" Priority="70" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Dark List Accent 1"/>\n  <w:LsdException Locked="false" Priority="71" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Colorful Shading Accent 1"/>\n  <w:LsdException Locked="false" Priority="72" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Colorful List Accent 1"/>\n  <w:LsdException Locked="false" Priority="73" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Colorful Grid Accent 1"/>\n  <w:LsdException Locked="false" Priority="60" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Light Shading Accent 2"/>\n  <w:LsdException Locked="false" Priority="61" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Light List Accent 2"/>\n  <w:LsdException Locked="false" Priority="62" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Light Grid Accent 2"/>\n  <w:LsdException Locked="false" Priority="63" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Medium Shading 1 Accent 2"/>\n  <w:LsdException Locked="false" Priority="64" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Medium Shading 2 Accent 2"/>\n  <w:LsdException Locked="false" Priority="65" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Medium List 1 Accent 2"/>\n  <w:LsdException Locked="false" Priority="66" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Medium List 2 Accent 2"/>\n  <w:LsdException Locked="false" Priority="67" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Medium Grid 1 Accent 2"/>\n  <w:LsdException Locked="false" Priority="68" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Medium Grid 2 Accent 2"/>\n  <w:LsdException Locked="false" Priority="69" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Medium Grid 3 Accent 2"/>\n  <w:LsdException Locked="false" Priority="70" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Dark List Accent 2"/>\n  <w:LsdException Locked="false" Priority="71" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Colorful Shading Accent 2"/>\n  <w:LsdException Locked="false" Priority="72" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Colorful List Accent 2"/>\n  <w:LsdException Locked="false" Priority="73" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Colorful Grid Accent 2"/>\n  <w:LsdException Locked="false" Priority="60" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Light Shading Accent 3"/>\n  <w:LsdException Locked="false" Priority="61" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Light List Accent 3"/>\n  <w:LsdException Locked="false" Priority="62" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Light Grid Accent 3"/>\n  <w:LsdException Locked="false" Priority="63" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Medium Shading 1 Accent 3"/>\n  <w:LsdException Locked="false" Priority="64" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Medium Shading 2 Accent 3"/>\n  <w:LsdException Locked="false" Priority="65" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Medium List 1 Accent 3"/>\n  <w:LsdException Locked="false" Priority="66" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Medium List 2 Accent 3"/>\n  <w:LsdException Locked="false" Priority="67" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Medium Grid 1 Accent 3"/>\n  <w:LsdException Locked="false" Priority="68" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Medium Grid 2 Accent 3"/>\n  <w:LsdException Locked="false" Priority="69" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Medium Grid 3 Accent 3"/>\n  <w:LsdException Locked="false" Priority="70" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Dark List Accent 3"/>\n  <w:LsdException Locked="false" Priority="71" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Colorful Shading Accent 3"/>\n  <w:LsdException Locked="false" Priority="72" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Colorful List Accent 3"/>\n  <w:LsdException Locked="false" Priority="73" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Colorful Grid Accent 3"/>\n  <w:LsdException Locked="false" Priority="60" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Light Shading Accent 4"/>\n  <w:LsdException Locked="false" Priority="61" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Light List Accent 4"/>\n  <w:LsdException Locked="false" Priority="62" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Light Grid Accent 4"/>\n  <w:LsdException Locked="false" Priority="63" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Medium Shading 1 Accent 4"/>\n  <w:LsdException Locked="false" Priority="64" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Medium Shading 2 Accent 4"/>\n  <w:LsdException Locked="false" Priority="65" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Medium List 1 Accent 4"/>\n  <w:LsdException Locked="false" Priority="66" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Medium List 2 Accent 4"/>\n  <w:LsdException Locked="false" Priority="67" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Medium Grid 1 Accent 4"/>\n  <w:LsdException Locked="false" Priority="68" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Medium Grid 2 Accent 4"/>\n  <w:LsdException Locked="false" Priority="69" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Medium Grid 3 Accent 4"/>\n  <w:LsdException Locked="false" Priority="70" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Dark List Accent 4"/>\n  <w:LsdException Locked="false" Priority="71" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Colorful Shading Accent 4"/>\n  <w:LsdException Locked="false" Priority="72" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Colorful List Accent 4"/>\n  <w:LsdException Locked="false" Priority="73" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Colorful Grid Accent 4"/>\n  <w:LsdException Locked="false" Priority="60" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Light Shading Accent 5"/>\n  <w:LsdException Locked="false" Priority="61" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Light List Accent 5"/>\n  <w:LsdException Locked="false" Priority="62" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Light Grid Accent 5"/>\n  <w:LsdException Locked="false" Priority="63" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Medium Shading 1 Accent 5"/>\n  <w:LsdException Locked="false" Priority="64" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Medium Shading 2 Accent 5"/>\n  <w:LsdException Locked="false" Priority="65" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Medium List 1 Accent 5"/>\n  <w:LsdException Locked="false" Priority="66" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Medium List 2 Accent 5"/>\n  <w:LsdException Locked="false" Priority="67" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Medium Grid 1 Accent 5"/>\n  <w:LsdException Locked="false" Priority="68" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Medium Grid 2 Accent 5"/>\n  <w:LsdException Locked="false" Priority="69" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Medium Grid 3 Accent 5"/>\n  <w:LsdException Locked="false" Priority="70" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Dark List Accent 5"/>\n  <w:LsdException Locked="false" Priority="71" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Colorful Shading Accent 5"/>\n  <w:LsdException Locked="false" Priority="72" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Colorful List Accent 5"/>\n  <w:LsdException Locked="false" Priority="73" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Colorful Grid Accent 5"/>\n  <w:LsdException Locked="false" Priority="60" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Light Shading Accent 6"/>\n  <w:LsdException Locked="false" Priority="61" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Light List Accent 6"/>\n  <w:LsdException Locked="false" Priority="62" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Light Grid Accent 6"/>\n  <w:LsdException Locked="false" Priority="63" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Medium Shading 1 Accent 6"/>\n  <w:LsdException Locked="false" Priority="64" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Medium Shading 2 Accent 6"/>\n  <w:LsdException Locked="false" Priority="65" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Medium List 1 Accent 6"/>\n  <w:LsdException Locked="false" Priority="66" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Medium List 2 Accent 6"/>\n  <w:LsdException Locked="false" Priority="67" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Medium Grid 1 Accent 6"/>\n  <w:LsdException Locked="false" Priority="68" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Medium Grid 2 Accent 6"/>\n  <w:LsdException Locked="false" Priority="69" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Medium Grid 3 Accent 6"/>\n  <w:LsdException Locked="false" Priority="70" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Dark List Accent 6"/>\n  <w:LsdException Locked="false" Priority="71" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Colorful Shading Accent 6"/>\n  <w:LsdException Locked="false" Priority="72" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Colorful List Accent 6"/>\n  <w:LsdException Locked="false" Priority="73" SemiHidden="false"\n   UnhideWhenUsed="false" Name="Colorful Grid Accent 6"/>\n  <w:LsdException Locked="false" Priority="19" SemiHidden="false"\n   UnhideWhenUsed="false" QFormat="true" Name="Subtle Emphasis"/>\n  <w:LsdException Locked="false" Priority="21" SemiHidden="false"\n   UnhideWhenUsed="false" QFormat="true" Name="Intense Emphasis"/>\n  <w:LsdException Locked="false" Priority="31" SemiHidden="false"\n   UnhideWhenUsed="false" QFormat="true" Name="Subtle Reference"/>\n  <w:LsdException Locked="false" Priority="32" SemiHidden="false"\n   UnhideWhenUsed="false" QFormat="true" Name="Intense Reference"/>\n  <w:LsdException Locked="false" Priority="33" SemiHidden="false"\n   UnhideWhenUsed="false" QFormat="true" Name="Book Title"/>\n  <w:LsdException Locked="false" Priority="37" Name="Bibliography"/>\n  <w:LsdException Locked="false" Priority="39" QFormat="true" Name="TOC Heading"/>\n </w:LatentStyles>\n</xml><![endif]--><!--[if gte mso 10]>\n<style>\n /* Style Definitions */\n table.MsoNormalTable\n\t{mso-style-name:"Tableau Normal";\n\tmso-tstyle-rowband-size:0;\n\tmso-tstyle-colband-size:0;\n\tmso-style-noshow:yes;\n\tmso-style-priority:99;\n\tmso-style-parent:"";\n\tmso-padding-alt:0cm 5.4pt 0cm 5.4pt;\n\tmso-para-margin:0cm;\n\tmso-para-margin-bottom:.0001pt;\n\tmso-pagination:widow-orphan;\n\tfont-size:10.0pt;\n\tfont-family:"Times New Roman","serif";}\n</style>\n<![endif]--></p>\n<p class="MsoNormal" style="mso-outline-level: 1;"><strong><span style="font-size: 11.0pt; font-family: \'Calibri\',\'sans-serif\'; mso-ansi-language: FR;" lang="FR">De&nbsp;:</span></strong><span style="font-size: 11.0pt; font-family: \'Calibri\',\'sans-serif\'; mso-ansi-language: FR;" lang="FR"> <a href="mailto:lino@example.com">lino@example.com</a> [<a href="mailto:lino@example.com">mailto:lino@example.com</a>] <br /> <strong>Envoy&eacute;&nbsp;:</strong> mardi 18 octobre 2016 08:52<br /> <strong>&Agrave;&nbsp;:</strong> <a href="mailto:aurelie@example.com">aurelie@example.com</a><br /> <strong>Objet&nbsp;:</strong> [welcht] Sandra modified sandra / Dupont T</span></p>\n<p class="MsoNormal">&nbsp;</p>\n<p>Dear Aur&eacute;lie,</p>\n<p>this is to notify you that Sandra  modified ssandra / Dupont T:</p>\n<p>Sandra modified <strong>sandra / Dupont T</strong></p>\n<p>TODO: include a summary of the modifications.</p>\n<p>Any subsequent notifications about sandra / Dupont T are suspended until you view this notification in the Lino web interface. Please visit</p>\n<p class="MsoNormal"><a href="None">None</a></p>\n<p>and follow your welcome messages.</p>\n<p>\n'

body = u'<p><!--[if gte foo 123]>A conditional comment<![endif]--></p>\n<p>Hello</p>'

from etgen.html import E, tostring
# E.names
# ALLOWED_TAGS = ['a', 'b', 'i', 'em', 'ul', 'ol', 'li', 'strong', 'p',
#                 'br', 'span', 'pre', 'def', 'style', 'table']
# body = bleach.clean(body, tags=E.names, strip=True)
ar = rt.login('robin')
elems = rich_text_to_elems(ar, body)
for e in elems:
    print(tostring(e))
